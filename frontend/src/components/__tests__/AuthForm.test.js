import React from 'react';
import { render, screen, fireEvent, waitFor } from '@testing-library/react';
import AuthForm from '../AuthForm';
import axios from 'axios';

jest.mock('axios');

describe('AuthForm Component', () => {
  it('validates email format', async () => {
    render(<AuthForm isLogin={true} />);
    
    fireEvent.input(screen.getByLabelText(/email/i), { 
      target: { value: 'invalid-email' }
    });
    fireEvent.submit(screen.getByRole('button'));
    
    expect(await screen.findByText(/invalid email/i)).toBeInTheDocument();
  });

  it('handles successful login', async () => {
    axios.post.mockResolvedValue({ data: { access_token: 'test-token' } });
    const mockNavigate = jest.fn();
    
    render(<AuthForm isLogin={true} navigate={mockNavigate} />);
    
    fireEvent.input(screen.getByLabelText(/email/i), { target: { value: 'test@ex.com' } });
    fireEvent.input(screen.getByLabelText(/password/i), { target: { value: 'password123' } });
    fireEvent.submit(screen.getByRole('button'));
    
    await waitFor(() => {
      expect(axios.post).toHaveBeenCalledWith(expect.stringContaining('/auth/login'), {
        username: 'test@ex.com',
        password: 'password123'
      });
      expect(mockNavigate).toHaveBeenCalledWith('/');
    });
  });
});
