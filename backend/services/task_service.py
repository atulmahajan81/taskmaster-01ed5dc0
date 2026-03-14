from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy.orm import selectinload
from uuid import UUID
from backend.models import Task
from backend.schemas import TaskCreate, TaskUpdate
from backend.cache import cache_with_ttl

class TaskService:
    """Service for task-related operations."""

    @cache_with_ttl(ttl=300)
    async def get_tasks(self, session: AsyncSession, skip: int = 0, limit: int = 10):
        """Retrieve tasks with pagination."""
        result = await session.execute(
            select(Task).offset(skip).limit(limit).options(selectinload(Task.user))
        )
        return result.scalars().all()

    async def create_task(self, session: AsyncSession, task_create: TaskCreate) -> Task:
        """Create a new task."""
        task = Task(**task_create.dict())
        session.add(task)
        await session.commit()
        await session.refresh(task)
        return task

    async def get_task_by_id(self, session: AsyncSession, task_id: UUID) -> Task:
        """Retrieve a task by ID."""
        result = await session.execute(select(Task).where(Task.id == task_id))
        return result.scalars().first()