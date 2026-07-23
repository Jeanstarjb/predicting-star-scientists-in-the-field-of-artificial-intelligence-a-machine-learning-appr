import React, { useState, useEffect } from 'react';
import { Box, Typography, useTheme, Grid, CircularProgress } from '@mui/material';
import { BarChart, Bar, XAxis, YAxis, CartesianGrid, Tooltip, Legend, ResponsiveContainer } from 'recharts';
import axios from 'axios';
import DiversityRadarChart from './DiversityRadarChart';

export default function InsightsDashboard() {
  const theme = useTheme();
  const [featureData, setFeatureData] = useState([]);
  const [diversityData, setDiversityData] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const fetchInsights = async () => {
      try {
        const [featuresRes, diversityRes] = await Promise.all([
          axios.get('/api/predict/feature-importance'),
          axios.get('/api/insights/diversity-metrics')
        ]);
        
        setFeatureData(featuresRes.data);
        setDiversityData(diversityRes.data);
        setLoading(false);
      } catch (error) {
        console.error('Error fetching insights:', error);
        setLoading(false);
      }
    };
    fetchInsights();
  }, []);

  if (loading) {
    return (
      <Box display="flex" justifyContent="center" mt={4}>
        <CircularProgress />
      </Box>
    );
  }

  return (
    <Box sx={{ p: 4 }}>
      <Typography variant="h4" gutterBottom sx={{ fontWeight: 600, color: theme.palette.primary.dark }}>
        Research Impact Analytics
      </Typography>
      
      <Grid container spacing={4}>
        <Grid item xs={12} md={6}>
          <Box sx={{ bgcolor: 'background.paper', p: 3, borderRadius: 4, boxShadow: theme.shadows[3] }}>
            <Typography variant="h6" gutterBottom sx={{ mb: 3, color: theme.palette.secondary.main }}>
              Model Feature Importance
            </Typography>
            <ResponsiveContainer width="100%" height={400}>
              <BarChart data={featureData}>
                <CartesianGrid strokeDasharray="3 3" />
                <XAxis
                  dataKey="feature"
                  angle={-45}
                  textAnchor="end"
                  tick={{ fill: theme.palette.text.primary }}
                />
                <YAxis tick={{ fill: theme.palette.text.primary }} />
                <Tooltip
                  contentStyle={{
                    backgroundColor: theme.palette.background.paper,
                    border: `1px solid ${theme.palette.divider}`,
                    borderRadius: theme.shape.borderRadius
                  }}
                />
                <Bar
                  dataKey="importance"
                  fill={theme.palette.primary.main}
                  radius={[4, 4, 0, 0]}
                />
              </BarChart>
            </ResponsiveContainer>
          </Box>
        </Grid>

        <Grid item xs={12} md={6}>
          <Box sx={{ bgcolor: 'background.paper', p: 3, borderRadius: 4, boxShadow: theme.shadows[3] }}>
            <Typography variant="h6" gutterBottom sx={{ mb: 3, color: theme.palette.secondary.main }}>
              Collaboration Diversity Profile
            </Typography>
            <DiversityRadarChart data={diversityData} />
          </Box>
        </Grid>
      </Grid>
    </Box>
  );
}