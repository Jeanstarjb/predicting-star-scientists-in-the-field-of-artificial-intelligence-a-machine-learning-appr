import React from 'react';
import { Radar, RadarChart, PolarGrid, PolarAngleAxis, PolarRadiusAxis, ResponsiveContainer } from 'recharts';
import { useTheme } from '@mui/material/styles';

export default function DiversityRadarChart({ data }) {
  const theme = useTheme();

  return (
    <ResponsiveContainer width="100%" height={400}>
      <RadarChart outerRadius="80%" data={data}>
        <PolarGrid stroke={theme.palette.divider} />
        <PolarAngleAxis
          dataKey="metric"
          tick={{ fill: theme.palette.text.primary }}
        />
        <PolarRadiusAxis
          angle={30}
          domain={[0, 1]}
          tick={{ fill: theme.palette.text.secondary }}
        />
        <Radar
          name="Diversity"
          dataKey="value"
          stroke={theme.palette.primary.main}
          fill={theme.palette.primary.main}
          fillOpacity={0.6}
        />
      </RadarChart>
    </ResponsiveContainer>
  );
}