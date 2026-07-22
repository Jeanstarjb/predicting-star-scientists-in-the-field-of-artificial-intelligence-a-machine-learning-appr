import React from 'react';
import { useFormik } from 'formik';
import * as Yup from 'yup';
import { Box, Button, Grid, TextField, Typography, Fade } from '@mui/material';
import axios from 'axios';

const validationSchema = Yup.object({
  name: Yup.string().required('Required'),
  institution: Yup.string().required('Required'),
  startYear: Yup.number().min(1950).max(new Date().getFullYear()).required('Required'),
  citationCount: Yup.number().min(0).required('Required'),
  publicationsCount: Yup.number().min(0).required('Required'),
  hIndex: Yup.number().min(0).required('Required'),
});

export default function ResearcherForm({ onSubmit, loading }) {
  const formik = useFormik({
    initialValues: {
      name: '',
      institution: '',
      startYear: '',
      citationCount: '',
      publicationsCount: '',
      hIndex: '',
    },
    validationSchema,
    onSubmit: async (values) => {
      onSubmit(values);
    },
  });

  return (
    <Box component="form" onSubmit={formik.handleSubmit} sx={{ mt: 4 }}>
      <Grid container spacing={3}>
        <Grid item xs={12} md={6}>
          <TextField
            fullWidth
            label="Researcher Name"
            variant="outlined"
            {...formik.getFieldProps('name')}
            error={formik.touched.name && Boolean(formik.errors.name)}
            helperText={formik.touched.name && formik.errors.name}
          />
        </Grid>
        <Grid item xs={12} md={6}>
          <TextField
            fullWidth
            label="Institution"
            variant="outlined"
            {...formik.getFieldProps('institution')}
            error={formik.touched.institution && Boolean(formik.errors.institution)}
            helperText={formik.touched.institution && formik.errors.institution}
          />
        </Grid>
        <Grid item xs={12} md={4}>
          <TextField
            fullWidth
            label="Start Year"
            type="number"
            variant="outlined"
            {...formik.getFieldProps('startYear')}
            error={formik.touched.startYear && Boolean(formik.errors.startYear)}
            helperText={formik.touched.startYear && formik.errors.startYear}
          />
        </Grid>
        <Grid item xs={12} md={4}>
          <TextField
            fullWidth
            label="Citations"
            type="number"
            variant="outlined"
            {...formik.getFieldProps('citationCount')}
            error={formik.touched.citationCount && Boolean(formik.errors.citationCount)}
            helperText={formik.touched.citationCount && formik.errors.citationCount}
          />
        </Grid>
        <Grid item xs={12} md={4}>
          <TextField
            fullWidth
            label="Publications"
            type="number"
            variant="outlined"
            {...formik.getFieldProps('publicationsCount')}
            error={formik.touched.publicationsCount && Boolean(formik.errors.publicationsCount)}
            helperText={formik.touched.publicationsCount && formik.errors.publicationsCount}
          />
        </Grid>
        <Grid item xs={12}>
          <TextField
            fullWidth
            label="H-Index"
            type="number"
            variant="outlined"
            {...formik.getFieldProps('hIndex')}
            error={formik.touched.hIndex && Boolean(formik.errors.hIndex)}
            helperText={formik.touched.hIndex && formik.errors.hIndex}
          />
        </Grid>
        <Grid item xs={12}>
          <Button
            type="submit"
            variant="contained"
            size="large"
            fullWidth
            disabled={loading}
            sx={{
              py: 2,
              bgcolor: 'primary.main',
              '&:hover': { bgcolor: 'primary.dark' },
              transition: 'all 0.3s ease',
            }}
          >
            {loading ? 'Analyzing...' : 'Predict Star Potential'}
          </Button>
        </Grid>
      </Grid>
    </Box>
  );
}
