import React from 'react';
import { useQuery } from '@tanstack/react-query';
import axios from 'axios';
import LoadingSpinner from './LoadingSpinner';
import ErrorBoundary from './ErrorBoundary';

interface DataTableProps {
    endpoint: string;
}

const DataTable: React.FC<DataTableProps> = ({ endpoint }) => {
    const { data, error, isLoading } = useQuery([endpoint], async () => {
        const response = await axios.get(endpoint);
        return response.data;
    });

    if (isLoading) return <LoadingSpinner />;
    if (error) return <div>Error loading data</div>;
    if (!data || data.length === 0) return <div>No data available</div>;

    return (
        <ErrorBoundary>
            <table className="min-w-full bg-white">
                <thead className="bg-gray-800 text-white">
                    <tr>
                        {/* Add table headers dynamically based on data structure */}
                    </tr>
                </thead>
                <tbody>
                    {data.map((item: any, index: number) => (
                        <tr key={index} className="text-center">
                            {/* Render data dynamically based on data structure */}
                        </tr>
                    ))}
                </tbody>
            </table>
        </ErrorBoundary>
    );
};

export default DataTable;