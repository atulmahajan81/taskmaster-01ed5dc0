import { useEffect } from 'react';
import { useRouter } from 'next/router';
import { useTask } from '../../lib/hooks/useTasks';
import { isAuthenticated } from '../../lib/auth';

const TaskDetailPage = () => {
  const router = useRouter();
  const { id } = router.query;
  const { data, error, isLoading } = useTask(id as string);

  useEffect(() => {
    if (!isAuthenticated()) {
      router.replace('/auth/login');
    }
  }, [router]);

  if (!isAuthenticated()) return null; // or a loading spinner

  if (isLoading) return <p>Loading task details...</p>;
  if (error) return <p>Error loading task.</p>;

  return (
    <div className="container mx-auto p-4">
      <h1 className="text-2xl font-bold mb-4">Task Details</h1>
      {data ? (
        <div>
          <h2 className="text-xl font-semibold">{data.title}</h2>
          <p>{data.description}</p>
          <p>Due Date: {new Date(data.due_date).toLocaleDateString()}</p>
        </div>
      ) : (
        <p>Task not found.</p>
      )}
    </div>
  );
};

export default TaskDetailPage;