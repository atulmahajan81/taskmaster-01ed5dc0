import axios from 'axios';
import { getToken, clearToken } from './auth';

export const api = axios.create({
  baseURL: (process.env.NEXT_PUBLIC_API_BASE_URL ?? 'http://localhost') + '/api/v1',
});

api.interceptors.request.use((config) => {
  const token = getToken();
  if (token) {
    config.headers.Authorization = `Bearer ${token}`;
  }
  return config;
});

api.interceptors.response.use(
  (response) => response,
  (error) => {
    if (error.response?.status === 401) {
      clearToken();
      window.location.href = '/auth/login';
    }
    return Promise.reject(error);
  }
);