import { useQuery } from '@tanstack/react-query';
import axios from 'axios';

export const useTasks = () => {
  return useQuery(['tasks'], async () => {
    const { data } = await axios.get('/api/v1/tasks');
    return data;
  });
};

export const useTask = (id: string) => {
  return useQuery(['task', id], async () => {
    const { data } = await axios.get(`/api/v1/tasks/${id}`);
    return data;
  });
};