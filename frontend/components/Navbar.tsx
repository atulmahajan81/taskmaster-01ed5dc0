import React from 'react';

const Navbar: React.FC = () => {
    return (
        <nav className="bg-white shadow px-4 py-2 flex items-center justify-between">
            <div className="text-xl font-semibold">TaskMaster</div>
            <div className="flex items-center">
                <div className="mr-4">Welcome, User</div>
                <button className="bg-blue-500 text-white px-3 py-1 rounded">Logout</button>
            </div>
        </nav>
    );
};

export default Navbar;