# test_tasks.py

import pytest

@pytest.mark.asyncio
async def test_create_task(async_client, user_token):
    """Test creating a new task with valid data"""
    response = await async_client.post(
        "/api/v1/tasks",
        headers={"Authorization": f"Bearer {user_token}"},
        json={"title": "New Task", "description": "Task description", "due_date": "2023-10-15"}
    )
    assert response.status_code == 201
    data = response.json()
    assert "task_id" in data

@pytest.mark.asyncio
async def test_list_tasks(async_client, user_token):
    """Test listing tasks for a user"""
    response = await async_client.get("/api/v1/tasks", headers={"Authorization": f"Bearer {user_token}"})
    assert response.status_code == 200
    data = response.json()
    assert "tasks" in data

@pytest.mark.asyncio
async def test_update_task(async_client, user_token):
    """Test updating an existing task"""
    task_response = await async_client.post(
        "/api/v1/tasks",
        headers={"Authorization": f"Bearer {user_token}"},
        json={"title": "Task to Update", "description": "Description", "due_date": "2023-10-15"}
    )
    task_id = task_response.json()["task_id"]
    response = await async_client.put(
        f"/api/v1/tasks/{task_id}",
        headers={"Authorization": f"Bearer {user_token}"},
        json={"title": "Updated Task", "description": "Updated Description", "due_date": "2023-11-01"}
    )
    assert response.status_code == 200
    data = response.json()
    assert data["task_id"] == task_id

@pytest.mark.asyncio
async def test_delete_task(async_client, user_token):
    """Test deleting a task"""
    task_response = await async_client.post(
        "/api/v1/tasks",
        headers={"Authorization": f"Bearer {user_token}"},
        json={"title": "Task to Delete", "description": "Description", "due_date": "2023-10-15"}
    )
    task_id = task_response.json()["task_id"]
    response = await async_client.delete(f"/api/v1/tasks/{task_id}", headers={"Authorization": f"Bearer {user_token}"})
    assert response.status_code == 200
    data = response.json()
    assert data["message"] == "Task deleted successfully"