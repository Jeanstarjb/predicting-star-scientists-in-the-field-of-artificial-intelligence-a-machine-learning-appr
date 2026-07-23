import React, { useState, useEffect } from 'react';
import { ThemeProvider, createTheme } from '@mui/material/styles';
import { CssBaseline, Container, Box } from '@mui/material';
import { BrowserRouter as Router, Route, Routes, Navigate } from 'react-router-dom';
import axios from 'axios';
import AuthForm from './components/AuthForm';
import ResearcherForm from './components/ResearcherForm';
import PredictionResult from './components/PredictionResult';
import Navigation from './components/Navigation';
import InsightsDashboard from './components/InsightsDashboard';

const theme = createTheme({
  palette: {
    mode: 'dark',
    primary: { main: '#7c4dff' },
    // ... [keep existing theme config] ...
});

function App() {
  const [user, setUser] = useState(null);

  useEffect(() => {
    const token = localStorage.getItem('accessToken');
    if (token) {
      axios.get('http://localhost:8000/auth/me', {
        headers: { Authorization: `Bearer ${token}` }
      }).then(res => setUser(res.data))
        .catch(() => localStorage.removeItem('accessToken'));
    }
  }, []);

  const ProtectedRoute = ({ children }) => {
    if (!user) {
      return <Navigate to="/login" replace />;
    }
    return children;
  };

  return (
    <ThemeProvider theme={theme}>
      <CssBaseline />
      <Router>
        <Navigation user={user} setUser={setUser} />
        <Container maxWidth="lg">
          <Routes>
            <Route path="/login" element={<AuthForm isLogin={true} />} />
            <Route path="/signup" element={<AuthForm isLogin={false} />} />
            <Route path="/" element={
              <ProtectedRoute>
                <ResearcherForm />
              </ProtectedRoute>
            } />
            <Route path="/insights" element={
              <ProtectedRoute>
                <InsightsDashboard />
              </ProtectedRoute>
            } />
          </Routes>
        </Container>
      </Router>
    </ThemeProvider>
  );
}

export default App;