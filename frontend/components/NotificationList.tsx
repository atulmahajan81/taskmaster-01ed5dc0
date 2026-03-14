import React from 'react';
import { useQuery } from '@tanstack/react-query';
import axios from 'axios';
import LoadingSpinner from './LoadingSpinner';

const fetchNotifications = async () => {
  const { data } = await axios.get('/api/notifications');
  return data;
};

const NotificationList: React.FC = () => {
  const { data, error, isLoading } = useQuery(['notifications'], fetchNotifications);

  if (isLoading) return <LoadingSpinner />;
  if (error) return <div>Error loading notifications.</div>;
  if (!data || data.length === 0) return <div>No notifications available.</div>;

  return (
    <div className="bg-white shadow-md rounded p-4">
      <h2 className="text-lg font-bold mb-4">Notifications</h2>
      <ul>
        {data.map((notification: any) => (
          <li key={notification.id} className="border-b py-2">
            {notification.message}
          </li>
        ))}
      </ul>
    </div>
  );
};

export default NotificationList;