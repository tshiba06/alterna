import axios from 'axios';

const api = axios.create({
  baseURL: 'http://localhost:18080',
});

export default api;
