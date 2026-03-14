import React from 'react';
import { useQuery } from '@tanstack/react-query';
import axios from 'axios';
import LoadingSpinner from './LoadingSpinner';

const fetchTasks = async () => {
  const { data } = await axios.get('/api/tasks');
  return data;
};

const TaskList: React.FC = () => {
  const { data, error, isLoading } = useQuery(['tasks'], fetchTasks);

  if (isLoading) return <LoadingSpinner />;
  if (error) return <div>Error loading tasks.</div>;
  if (!data || data.length === 0) return <div>No tasks available.</div>;

  return (
    <div className="bg-white shadow-md rounded p-4">
      <h2 className="text-lg font-bold mb-4">Tasks</h2>
      <ul>
        {data.map((task: any) => (
          <li key={task.id} className="border-b py-2">
            {task.title}
          </li>
        ))}
      </ul>
    </div>
  );
};

export default TaskList;