import React from 'react';

interface ResourceCardProps {
    title: string;
    description: string;
    priority: string;
    isCompleted: boolean;
}

const ResourceCard: React.FC<ResourceCardProps> = ({ title, description, priority, isCompleted }) => {
    return (
        <div className={`p-4 border rounded shadow-md ${isCompleted ? 'bg-green-100' : 'bg-white'}`}>
            <h3 className="text-lg font-semibold">{title}</h3>
            <p className="text-gray-700">{description}</p>
            <div className="mt-2">
                <span className="text-sm text-gray-500">Priority: {priority}</span>
            </div>
            <div className="mt-2">
                <span className={`text-sm ${isCompleted ? 'text-green-600' : 'text-red-600'}`}>{isCompleted ? 'Completed' : 'Pending'}</span>
            </div>
        </div>
    );
};

export default ResourceCard;