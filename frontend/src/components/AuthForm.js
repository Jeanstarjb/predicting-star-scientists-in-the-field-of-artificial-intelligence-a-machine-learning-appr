import React, { useState } from 'react';
import { useFormik } from 'formik';
import * as Yup from 'yup';
import { Box, Button, TextField, Typography, Fade, CircularProgress, Link } from '@mui/material';
import axios from 'axios';
import { useNavigate } from 'react-router-dom';

const AuthForm = ({ isLogin }) => {
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');
  const navigate = useNavigate();

  const validationSchema = Yup.object({
    email: Yup.string().email('Invalid email').required('Required'),
    password: Yup.string().min(8, 'Minimum 8 characters').required('Required'),
    ...(!isLogin && {
      confirmPassword: Yup.string()
        .oneOf([Yup.ref('password'), null], 'Passwords must match')
        .required('Required')
    })
  });

  const handleSubmit = async (values) => {
    setLoading(true);
    try {
      const endpoint = isLogin ? '/auth/login' : '/auth/signup';
      const response = await axios.post(`http://localhost:8000${endpoint}`, {
        ...(isLogin ? {
          username: values.email,
          password: values.password
        } : {
          email: values.email,
          password: values.password
        })
      });

      if (isLogin) {
        localStorage.setItem('accessToken', response.data.access_token);
        navigate('/');
      } else {
        navigate('/login');
      }
    } catch (err) {
      setError(err.response?.data?.detail || 'An error occurred');
    } finally {
      setLoading(false);
    }
  };

  return (
    <Fade in={true}>
      <Box sx={{ maxWidth: 400, mx: 'auto', mt: 8, p: 4, bgcolor: 'background.paper', borderRadius: 4 }}>
        <Typography variant="h4" gutterBottom sx={{ fontWeight: 700, color: 'primary.main' }}>
          {isLogin ? 'Welcome Back' : 'Get Started'}
        </Typography>
        
        <form onSubmit={formik.handleSubmit}>
          <TextField
            fullWidth
            margin="normal"
            label="Email"
            name="email"
            variant="outlined"
            {...formik.getFieldProps('email')}
            error={formik.touched.email && Boolean(formik.errors.email)}
            helperText={formik.touched.email && formik.errors.email}
          />
          <TextField
            fullWidth
            margin="normal"
            label="Password"
            name="password"
            type="password"
            variant="outlined"
            {...formik.getFieldProps('password')}
            error={formik.touched.password && Boolean(formik.errors.password)}
            helperText={formik.touched.password && formik.errors.password}
          />
          {!isLogin && (
            <TextField
              fullWidth
              margin="normal"
              label="Confirm Password"
              name="confirmPassword"
              type="password"
              variant="outlined"
              {...formik.getFieldProps('confirmPassword')}
              error={formik.touched.confirmPassword && Boolean(formik.errors.confirmPassword)}
              helperText={formik.touched.confirmPassword && formik.errors.confirmPassword}
            />
          )}
          
          {error && (
            <Typography color="error" sx={{ mt: 2 }}>
              {error}
            </Typography>
          )}
          
          <Button
            fullWidth
            variant="contained"
            size="large"
            type="submit"
            disabled={loading}
            sx={{ mt: 3, py: 1.5, fontWeight: 600 }}
          >
            {loading ? <CircularProgress size={24} /> : (isLogin ? 'Sign In' : 'Create Account')}
          </Button>
          
          <Box sx={{ mt: 3, textAlign: 'center' }}>
            <Link href={isLogin ? '/signup' : '/login'} sx={{ cursor: 'pointer' }}>
              {isLogin ? 'Need an account? Sign Up' : 'Already have an account? Sign In'}
            </Link>
          </Box>
        </form>
      </Box>
    </Fade>
  );
};

export default AuthForm;