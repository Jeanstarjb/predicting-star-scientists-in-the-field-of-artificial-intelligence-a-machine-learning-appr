import React from 'react';
import { AppBar, Toolbar, Typography, Button, Container } from '@mui/material';
import { Link } from 'react-router-dom';

export default function Navigation() {
  return (
    <AppBar position="static" sx={{ mb: 4, bgcolor: 'background.paper' }}>
      <Container maxWidth="lg">
        <Toolbar disableGutters>
          <Typography 
            variant="h6" 
            component={Link} 
            to="/"
            sx={{
              flexGrow: 1,
              textDecoration: 'none',
              color: 'primary.main',
              fontWeight: 800,
              '&:hover': { color: 'primary.dark' },
            }}
          >
            StarFinder
          </Typography>
          <Button 
            component={Link} 
            to="/insights"
            sx={{
              color: 'text.primary',
              '&:hover': { color: 'primary.main' },
              transition: 'color 0.3s ease',
            }}
          >
            Insights
          </Button>
        </Toolbar>
      </Container>
    </AppBar>
  );
}
