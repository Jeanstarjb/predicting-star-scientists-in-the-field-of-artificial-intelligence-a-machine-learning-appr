import React from 'react';
import { render, screen } from '@testing-library/react';
import PredictionResult from '../PredictionResult';
import { BarChart } from 'recharts';

describe('PredictionResult Component', () => {
  const mockData = {
    probability: 0.85,
    feature_importances: [
      { feature: 'citations', importance: 0.4 },
      { feature: 'grants', importance: 0.3 }
    ]
  };

  it('displays prediction probability correctly', () => {
    render(<PredictionResult data={mockData} />);
    
    expect(screen.getByText(/85%/i)).toBeInTheDocument();
    expect(screen.getByText(/high potential/i)).toBeInTheDocument();
  });

  it('renders feature importance chart', () => {
    const { container } = render(<PredictionResult data={mockData} />);
    
    expect(container.querySelector('.recharts-bar')).toBeInTheDocument();
    expect(screen.getByText('citations')).toBeInTheDocument();
  });
});
