import { createTheme } from '@mui/material/styles';

// Color definitions from quasar.variables.scss
const primaryColor = '#1976d2';
const secondaryColor = '#26a69a';
const accentColor = '#9c27b0'; // Will map to secondary or a custom field

const positiveColor = '#21ba45';
const negativeColor = '#c10015';
const infoColor = '#31ccec';
const warningColor = '#f2c037';

// Dark theme specific colors (for reference or future dark mode)
// const darkBackgroundColor = '#121212';
// const darkTextColor = '#1d1d1d'; // This might be too dark for primary text on dark bg, often light text is used.

const theme = createTheme({
  palette: {
    primary: {
      main: primaryColor,
    },
    secondary: {
      // Using accentColor for secondary as MUI's secondary is the closest equivalent
      // or if $secondary from Quasar is more fitting, use that.
      // Given $secondary: #26a69a is defined, it's better to use it.
      main: secondaryColor, 
    },
    // If accent needs to be distinct and used, it can be added as a custom color:
    // accent: { // This requires module augmentation to be typed correctly
    //   main: accentColor,
    // },
    error: {
      main: negativeColor,
    },
    warning: {
      main: warningColor,
    },
    info: {
      main: infoColor,
    },
    success: {
      main: positiveColor,
    },
    // Example for dark mode (if we were to implement a toggle)
    // background: {
    //   default: lightMode ? '#ffffff' : darkBackgroundColor,
    //   paper: lightMode ? '#ffffff' : darkBackgroundColor,
    // },
    // text: {
    //   primary: lightMode ? 'rgba(0, 0, 0, 0.87)' : '#ffffff',
    //   secondary: lightMode ? 'rgba(0, 0, 0, 0.6)' : 'rgba(255, 255, 255, 0.7)',
    // },
  },
  // You can also customize typography, spacing, breakpoints, etc.
  // typography: {
  //   fontFamily: 'Roboto, Arial, sans-serif',
  // },
  // spacing: 8, // Default is 8
});

// To make 'accent' available in the palette and typed correctly,
// you would need module augmentation like this (typically in a d.ts file):
/*
declare module '@mui/material/styles' {
  interface Palette {
    accent?: Palette['primary'];
  }
  interface PaletteOptions {
    accent?: PaletteOptions['primary'];
  }
}
declare module '@mui/material/Button' {
  interface ButtonPropsColorOverrides {
    accent: true;
  }
}
*/

export default theme;
