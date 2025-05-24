import React from 'react';
import { RouterProvider } from 'react-router-dom';
import { ThemeProvider } from '@mui/material/styles';
import CssBaseline from '@mui/material/CssBaseline'; // Good to have it here for global effect
import router from './router';
import theme from './styles/theme'; // Import the custom theme
import './App.css'; // Assuming you might have some global styles here

const App: React.FC = () => {
  return (
    <ThemeProvider theme={theme}>
      <CssBaseline /> {/* Ensures baseline styles and theme background are applied globally */}
      <RouterProvider router={router} />
    </ThemeProvider>
  );
};

export default App;
