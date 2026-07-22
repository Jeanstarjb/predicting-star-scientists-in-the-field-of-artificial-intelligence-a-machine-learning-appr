import React, { useState } from 'react';
import { ThemeProvider, createTheme } from '@mui/material/styles';
import { CssBaseline, Container, Box } from '@mui/material';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import axios from 'axios';
import ResearcherForm from './components/ResearcherForm';
import PredictionResult from './components/PredictionResult';
import Navigation from './components/Navigation';
import InsightsDashboard from './components/InsightsDashboard';

const theme = createTheme({
  palette: {
    mode: 'dark',
    primary: { main: '#7c4dff' },
    secondary: { main: '#00bcd4' },
    background: { default: '#121212', paper: '#1e1e1e' },
  },
  typography: {
    fontFamily: 'Inter, sans-serif',
    h1: { fontWeight: 800, fontSize: '3.5rem' },
  },
  shape: { borderRadius: 16 },
});

export default function App() {
  const [prediction, setPrediction] = useState(null);
  const [loading, setLoading] = useState(false);

  const handlePredict = async (data) => {
    setLoading(true);
    try {
      const response = await axios.post('http://localhost:8000/predict', data);
      setPrediction(response.data);
    } catch (error) {
      console.error('Prediction error:', error);
    } finally {
      setLoading(false);
    }
  };

  return (
    <ThemeProvider theme={theme}>
      <CssBaseline />
      <Router>
        <Navigation />
        <Container maxWidth="md" sx={{ py: 6 }}>
          <Routes>
            <Route path="/" element={
              <>
                <Box sx={{ textAlign: 'center', mb: 6 }}>
                  <Typography variant="h1" gutterBottom>
                    Star Scientist Predictor
                  </Typography>
                  <Typography variant="h5" color="text.secondary">
                    Identify future AI research leaders through early-career achievements
                  </Typography>
                </Box>
                <ResearcherForm onSubmit={handlePredict} loading={loading} />
                <PredictionResult prediction={prediction} loading={loading} />
              </>
            } />
            <Route path="/insights" element={<InsightsDashboard />} />
          </Routes>
        </Container>
      </Router>
    </ThemeProvider>
  );
}
