import React from 'react';
import { useRouter } from 'next/router';

const Sidebar: React.FC = () => {
    const router = useRouter();
    const links = [
        { name: 'Dashboard', path: '/' },
        { name: 'Tasks', path: '/tasks' },
        { name: 'Notifications', path: '/notifications' },
    ];

    return (
        <aside className="bg-gray-800 text-gray-100 w-64 space-y-6 py-7 px-2">
            <nav className="space-y-1">
                {links.map(link => (
                    <a
                        key={link.name}
                        href={link.path}
                        className={`block py-2.5 px-4 rounded transition duration-200 hover:bg-gray-700 ${router.pathname === link.path ? 'bg-gray-700' : ''}`}
                    >
                        {link.name}
                    </a>
                ))}
            </nav>
        </aside>
    );
};

export default Sidebar;