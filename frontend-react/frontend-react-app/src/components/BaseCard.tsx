import React from 'react';
import Card from '@mui/material/Card';
import CardActions from '@mui/material/CardActions';
import CardContent from '@mui/material/CardContent';
import Button from '@mui/material/Button';
import Typography from '@mui/material/Typography';
import CircularProgress from '@mui/material/CircularProgress';
import Backdrop from '@mui/material/Backdrop';
// Removed Box import as it's not strictly necessary if CardActions handles layout

interface BaseCardProps {
  total: number;
  title: string;
  bgColor: string;
  loading: boolean;
  onClickUpdate: () => void;
}

const BaseCard: React.FC<BaseCardProps> = ({
  total,
  title,
  bgColor,
  loading,
  onClickUpdate,
}) => {
  return (
    <Card sx={{ position: 'relative', minWidth: 275, borderRadius: 2 }}> {/* Added slight borderRadius for aesthetics */}
      <CardActions sx={{ 
        backgroundColor: bgColor, 
        justifyContent: 'flex-end', 
        padding: '8px',
        // Ensure CardActions is above CardContent if they were to overlap (not typical)
        // borderTopLeftRadius: (theme) => theme.shape.borderRadius, // if card has border radius
        // borderTopRightRadius: (theme) => theme.shape.borderRadius,
        }}>
        <Button
          variant="contained" // Using contained for a more distinct button feel
          onClick={onClickUpdate}
          sx={{
            backgroundColor: 'white',
            color: 'rgba(0, 0, 0, 0.87)', // Default text color for contrast on white
            border: '1px solid rgba(0, 0, 0, 0.23)', // Subtle border like outlined
            borderRadius: '50%', 
            minWidth: 'auto', 
            width: 40, 
            height: 40, 
            padding: 0,
            boxShadow: 'none', // Remove default elevation for a flatter look
            '&:hover': {
              backgroundColor: '#f0f0f0', // Slightly darker hover for white button
              boxShadow: 'none', // Keep it flat on hover
            },
            // For "text-with-outline", the border serves as an outline.
            // If a more pronounced text outline is needed, it's more complex (e.g., text-shadow)
            // but this setup provides a white button with dark text and a border.
          }}
        >
          更新
        </Button>
      </CardActions>
      <CardContent sx={{ paddingTop: '16px', paddingBottom: '16px' }}> {/* Adjusted padding */}
        <Typography sx={{ fontSize: 16, marginBottom: 1 }} color="text.secondary" gutterBottom>
          {title}
        </Typography>
        <Typography variant="h4" component="div">
          {total.toLocaleString()} 円
        </Typography>
      </CardContent>
      <Backdrop
        sx={{
          color: '#fff',
          zIndex: (theme) => theme.zIndex.modal + 1, // Ensure it's above other card content
          position: 'absolute', 
          top: 0,
          left: 0,
          right: 0,
          bottom: 0,
          backgroundColor: 'rgba(0, 0, 0, 0.4)', // Slightly adjusted opacity
          borderRadius: 'inherit', // Inherit border radius from parent Card
        }}
        open={loading}
      >
        <CircularProgress color="inherit" />
      </Backdrop>
    </Card>
  );
};

export default BaseCard;
