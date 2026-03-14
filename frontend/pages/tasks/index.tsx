import { useEffect } from 'react';
import { useRouter } from 'next/router';
import { useTasks } from '../../lib/hooks/useTasks';
import { isAuthenticated } from '../../lib/auth';

const TasksPage = () => {
  const router = useRouter();
  const { data, error, isLoading } = useTasks();

  useEffect(() => {
    if (!isAuthenticated()) {
      router.replace('/auth/login');
    }
  }, [router]);

  if (!isAuthenticated()) return null; // or a loading spinner

  if (isLoading) return <p>Loading...</p>;
  if (error) return <p>Error loading tasks.</p>;

  return (
    <div className="container mx-auto p-4">
      <h1 className="text-2xl font-bold mb-4">Your Tasks</h1>
      {data && data.tasks.length > 0 ? (
        <ul>
          {data.tasks.map((task) => (
            <li key={task.id} className="mb-2">
              {task.title}
            </li>
          ))}
        </ul>
      ) : (
        <p>No tasks available.</p>
      )}
    </div>
  );
};

export default TasksPage;