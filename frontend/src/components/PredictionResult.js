import React from 'react';
import { Box, Typography, CircularProgress, useTheme, Fade } from '@mui/material';
import CheckCircleOutlineIcon from '@mui/icons-material/CheckCircleOutline';
import HighlightOffIcon from '@mui/icons-material/HighlightOff';

export default function PredictionResult({ prediction, loading }) {
  const theme = useTheme();
  
  if (loading) return (
    <Box sx={{ display: 'flex', justifyContent: 'center', mt: 4 }}>
      <CircularProgress size={60} thickness={4} />
    </Box>
  );

  if (!prediction) return null;

  const isStar = prediction.starPotential >= 0.7;
  const color = isStar ? theme.palette.success.main : theme.palette.error.main;

  return (
    <Fade in={true} timeout={500}>
      <Box sx={{
        mt: 4,
        p: 4,
        borderRadius: 4,
        background: `linear-gradient(145deg, ${color}20, ${color}30)`,
        border: `1px solid ${color}30`,
        backdropFilter: 'blur(10px)',
      }}>
        <Box sx={{
          display: 'flex',
          alignItems: 'center',
          mb: 2,
          gap: 2
        }}>
          {isStar ? (
            <CheckCircleOutlineIcon sx={{ fontSize: 40, color }} />
          ) : (
            <HighlightOffIcon sx={{ fontSize: 40, color }} />
          )}
          <Typography variant="h4" component="div" sx={{ color }}>
            {isStar ? 'Star Potential Detected!' : 'Needs More Development'}
          </Typography>
        </Box>
        <Typography variant="h2" sx={{ fontWeight: 800, color }}>
          {(prediction.starPotential * 100).toFixed(1)}%
        </Typography>
        <Typography variant="body1" sx={{ mt: 2, color: 'text.secondary' }}>
          Key contributing factors:
        </Typography>
        <Box component="ul" sx={{ pl: 3, mt: 1 }}>
          {prediction.featureContributions.map((feature, i) => (
            <li key={i}>
              <Typography variant="body2">
                {feature.name}: {feature.value.toFixed(2)}
              </Typography>
            </li>
          ))}
        </Box>
      </Box>
    </Fade>
  );
}
