from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List
from uuid import UUID
from backend.schemas import TaskCreate, TaskUpdate, TaskResponse, MessageResponse
from backend.services.task_service import TaskService
from backend.database import get_async_session

router = APIRouter()

task_service = TaskService()


@router.get('/list', response_model=List[TaskResponse], response_model_exclude_unset=True)
async def list_tasks(
    skip: int = 0,
    limit: int = 10,
    session: AsyncSession = Depends(get_async_session)
):
    """Retrieve a list of tasks with pagination."""
    return await task_service.get_tasks(session, skip=skip, limit=limit)


@router.post('/create', response_model=TaskResponse)
async def create_task(
    task: TaskCreate,
    session: AsyncSession = Depends(get_async_session)
):
    """Create a new task."""
    return await task_service.create_task(session, task)


@router.get('/{task_id}', response_model=TaskResponse)
async def get_task(
    task_id: UUID,
    session: AsyncSession = Depends(get_async_session)
):
    """Retrieve a task by its ID."""
    task = await task_service.get_task_by_id(session, task_id)
    if task is N