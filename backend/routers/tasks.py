from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from uuid import UUID
from typing import List

from backend.database import get_session
from backend.models import Task
from backend.schemas import TaskCreate, TaskUpdate, TaskOut
from backend.services.task_service import TaskService
from backend.dependencies import get_current_user

router = APIRouter()


@router.get("/", response_model=List[TaskOut])
async def list_tasks(
    skip: int = 0,
    limit: int = 10,
    search: str = None,
    current_user: UUID = Depends(get_current_user),
    db: AsyncSession = Depends(get_session)
):
    """
    Retrieve a list of tasks for the authenticated user.
    """
    tasks = await TaskService.list_tasks(db, current_user, skip, limit, search)
    return tasks


@router.post("/", response_model=TaskOut)
async def create_task(
    task_in: TaskCreate,
    current_user: UUID = Depends(get_current_user),
    db: AsyncSession = Depends(get_session)
):
    """
    Create a new task for the authenticated user.
    """
    task = await TaskService.create_task(db, current_user, task_in)
    return task


@router.put("/{task_id}", response_model=TaskOut)
async def update_task(
    task_id: UUID,
    task_in: TaskUpdate,
    current_user: UUID = Depends(get_current_user),
    db: AsyncSession = Depends(get_session)
):
    """
    Update an existing task.
    """
    task = await TaskService.update_task(db, current_user, task_id, task_in)
    if not task:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Task not found")
    return task


@router.delete("/{task_id}")
async def delete_task(
    task_id: UUID,
    current_user: UUID = Depends(get_current_user),
    db: AsyncSession = Depends(get_session)
):
    """
    Delete a task.
    """
    success = await TaskService.delete_task(db, current_user, task_id)
    if not success:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Task not found")
    return {"message": "Task deleted successfully"}


@router.patch("/{task_id}/complete", response_model=TaskOut)
async def complete_task(
    task_id: UUID,
    current_user: UUID = Depends(get_current_user),
    db: AsyncSession = Depends(get_session)
):
    """
    Mark a task as completed.
    """
    task = await TaskService.complete_task(db, current_user, task_id)
    if not task:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Task not found")
    return task


@router.patch("/{task_id}/priority", response_model=TaskOut)
async def set_task_priority(
    task_id: UUID,
    priority: str,
    current_user: UUID = Depends(get_current_user),
    db: AsyncSession = Depends(get_session)
):
    """
    Set the priority of a task.
    """
    task = await TaskService.set_priority(db, current_user, task_id, priority)
    if not task:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Task not found")
    return task