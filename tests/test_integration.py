# test_integration.py

import pytest

@pytest.mark.asyncio
async def test_full_user_task_flow(async_client):
    """Test complete user flow: Register -> Login -> Create Task -> List -> Update -> Delete"""
    # Register
    register_response = await async_client.post("/api/v1/auth/register", json={"email": "flow@test.com", "password": "flowpassword"})
    assert register_response.status_code == 201
    
    # Login
    login_response = await async_client.post("/api/v1/auth/login", json={"email": "flow@test.com", "password": "flowpassword"})
    assert login_response.status_code == 200
    tokens = login_response.json()
    access_token = tokens["access_token"]
    
    # Create Task
    create_response = await async_client.post(
        "/api/v1/tasks",
        headers={"Authorization": f"Bearer {access_token}"},
        json={"title": "Flow Task", "description": "Task Description", "due_date": "2023-11-15"}
    )
    assert create_response.status_code == 201
    task_id = create_response.json()["task_id"]
    
    # List Tasks
    list_response = await async_client.get("/api/v1/tasks", headers={"Authorization": f"Bearer {access_token}"})
    assert list_response.status_code == 200
    assert any(task["task_id"] == task_id for task in list_response.json()["tasks"])
    
    # Update Task
    update_response = await async_client.put(
        f"/api/v1/tasks/{task_id}",
        headers={"Authorization": f"Bearer {access_token}"},
        json={"title": "Updated Flow Task", "description": "Updated Description", "due_date": "2023-12-01"}
    )
    assert update_response.status_code == 200
    
    # Delete Task
    delete_response = await async_client.delete(f"/api/v1/tasks/{task_id}", headers={"Authorization": f"Bearer {access_token}"})
    assert delete_response.status_code == 200