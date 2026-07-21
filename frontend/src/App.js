import React, { useState } from 'react';
import { ThemeProvider, createTheme } from '@mui/material/styles';
import { Container, CssBaseline, Typography, Button, Paper, CircularProgress } from '@mui/material';
import axios from 'axios';

const theme = createTheme({
  palette: {
    mode: 'light',
    primary: {
      main: '#2e7d32',
    },
    secondary: {
      main: '#d84315',
    },
  },
});

export default function App() {
  const [prediction, setPrediction] = useState(null);
  const [loading, setLoading] = useState(false);

  const handlePredict = async () => {
    setLoading(true);
    try {
      const response = await axios.post('/api/predict', {
        features: [] // Placeholder for actual features
      });
      setPrediction(response.data);
    } catch (error) {
      console.error('Prediction error:', error);
    }
    setLoading(false);
  };

  return (
    <ThemeProvider theme={theme}>
      <CssBaseline />
      <Container maxWidth="md" sx={{ py: 4 }}>
        <Paper elevation={3} sx={{ p: 4, textAlign: 'center' }}>
          <Typography variant="h4" gutterBottom sx={{ color: 'primary.main' }}>
            Star Scientist Predictor
          </Typography>
          <Button
            variant="contained"
            onClick={handlePredict}
            disabled={loading}
            sx={{ mt: 2 }}
          >
            {loading ? <CircularProgress size={24} /> : 'Run Prediction'}
          </Button>
          {prediction && (
            <Typography variant="h6" sx={{ mt: 4, color: 'secondary.main' }}>
              Prediction Score: {prediction.prediction}
            </Typography>
          )}
        </Paper>
      </Container>
    </ThemeProvider>
  );
}