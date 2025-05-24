import React from 'react';
import { Outlet } from 'react-router-dom';
import AppBar from '@mui/material/AppBar';
import Toolbar from '@mui/material/Toolbar';
import IconButton from '@mui/material/IconButton';
import Typography from '@mui/material/Typography';
import MenuIcon from '@mui/icons-material/Menu';
import Box from '@mui/material/Box';
import Container from '@mui/material/Container';
// Recommended for baseline styling - Removed as it's now in App.tsx

const MainLayout: React.FC = () => {
  return (
    <Box sx={{ display: 'flex', flexDirection: 'column', minHeight: '100vh' }}>
      {/* Apply baseline browser styling normalization - Removed as it's now in App.tsx */}
      <AppBar position="static">
        <Toolbar>
          <IconButton
            size="large"
            edge="start"
            color="inherit"
            aria-label="menu"
            sx={{ mr: 2 }}
            // onClick={() => console.log('Menu button clicked')} // Placeholder action
          >
            <MenuIcon />
          </IconButton>
          <Typography variant="h6" component="div" sx={{ flexGrow: 1 }}>
            Alterna
          </Typography>
          {/* Future toolbar items can be added here */}
        </Toolbar>
      </AppBar>
      <Container component="main" sx={{ flexGrow: 1, py: 3 }}> {/* py: padding top/bottom */}
        <Outlet /> {/* This is where child routes will be rendered */}
      </Container>
      {/* Optional: A Box component could be used as a footer here */}
    </Box>
  );
};

export default MainLayout;
