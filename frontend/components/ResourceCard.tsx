import React from 'react';

interface ResourceCardProps {
  title: string;
  description: string;
  status: 'completed' | 'pending';
}

const ResourceCard: React.FC<ResourceCardProps> = ({ title, description, status }) => {
  return (
    <div className="border rounded shadow-sm p-4 bg-white">
      <h2 className="text-lg font-semibold mb-2">{title}</h2>
      <p className="text-gray-700 mb-4">{description}</p>
      <span className={`px-2 py-1 inline-block rounded ${status === 'completed' ? 'bg-green-200 text-green-800' : 'bg-yellow-200 text-yellow-800'}`}>
        {status === 'completed' ? 'Completed' : 'Pending'}
      </span>
    </div>
  );
};

export default ResourceCard;