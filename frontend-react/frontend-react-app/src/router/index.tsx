import React from 'react';
import { createBrowserRouter, RouteObject } from 'react-router-dom';
import MainLayout from '../layouts/MainLayout';
import IndexPage from '../pages/IndexPage';
import ErrorNotFound from '../pages/ErrorNotFound';

export const routes: RouteObject[] = [
  {
    path: '/',
    element: <MainLayout />,
    children: [
      {
        index: true,
        element: <IndexPage />,
      },
    ],
  },
  {
    path: '*',
    element: <ErrorNotFound />,
  },
];

const router = createBrowserRouter(routes);

export default router;
