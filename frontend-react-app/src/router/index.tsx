import type { RouteObject } from 'react-router-dom';
import { createBrowserRouter } from 'react-router-dom';
import MainLayout from '../layouts/MainLayout';
import ErrorNotFound from '../pages/ErrorNotFound';
import IndexPage from '../pages/IndexPage';

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
