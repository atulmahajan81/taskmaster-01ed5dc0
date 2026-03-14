import React from 'react';
import { useMutation, useQueryClient } from '@tanstack/react-query';
import axios from 'axios';

const TaskForm: React.FC = () => {
  const queryClient = useQueryClient();
  const mutation = useMutation(
    (newTask: { title: string }) => axios.post('/api/tasks', newTask),
    {
      onSuccess: () => queryClient.invalidateQueries(['tasks']),
    }
  );

  const handleSubmit = (event: React.FormEvent) => {
    event.preventDefault();
    const formData = new FormData(event.target as HTMLFormElement);
    const title = formData.get('title') as string;
    mutation.mutate({ title });
  };

  return (
    <form onSubmit={handleSubmit} className="bg-white shadow-md rounded p-4 mb-4">
      <h2 className="text-lg font-bold mb-4">Add New Task</h2>
      <input
        type="text"
        name="title"
        placeholder="Task title"
        className="border py-2 px-3 w-full mb-4"
        required
      />
      <button
        type="submit"
        className="bg-blue-500 text-white px-4 py-2 rounded hover:bg-blue-700"
      >
        Add Task
      </button>
    </form>
  );
};

export default TaskForm;