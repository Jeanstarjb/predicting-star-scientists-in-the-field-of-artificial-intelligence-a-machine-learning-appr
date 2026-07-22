import React from 'react';
import { Box, Typography, useTheme } from '@mui/material';
import { BarChart, Bar, XAxis, YAxis, CartesianGrid, Tooltip, Legend, ResponsiveContainer } from 'recharts';

export default function InsightsDashboard() {
  const theme = useTheme();

  const featureData = [
    { name: 'Publications', value: 0.32 },
    { name: 'Citations', value: 0.28 },
    { name: 'H-Index', value: 0.24 },
    { name: 'Diversity', value: 0.16 },
  ];

  return (
    <Box sx={{ mt: 4 }}>
      <Typography variant="h4" gutterBottom>
        Feature Importance Analysis
      </Typography>
      <Box sx={{ height: 400, mt: 4 }}>
        <ResponsiveContainer width="100%" height="100%">
          <BarChart data={featureData}>
            <CartesianGrid strokeDasharray="3 3" />
            <XAxis dataKey="name" />
            <YAxis />
            <Tooltip />
            <Bar 
              dataKey="value" 
              fill={theme.palette.primary.main}
              radius={[4, 4, 0, 0]}
            />
          </BarChart>
        </ResponsiveContainer>
      </Box>
      <Typography variant="h4" gutterBottom sx={{ mt: 6 }}>
        Top Performing Researchers
      </Typography>
      {/* Add researcher leaderboard component here */}
    </Box>
  );
}
