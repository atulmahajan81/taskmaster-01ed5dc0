# test_services.py

import pytest
from backend.services.task_service import create_task

@pytest.mark.asyncio
async def test_create_task_service(test_db):
    """Test task creation service method"""
    async with test_db() as db:
        task_data = {"title": "Service Task", "description": "Task Description", "due_date": "2023-10-15", "user_id": "valid-user-id"}
        task = await create_task(db, **task_data)
        assert task.title == "Service Task"
        assert task.description == "Task Description"