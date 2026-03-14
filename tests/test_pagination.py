# test_pagination.py

import pytest

@pytest.mark.asyncio
async def test_task_pagination(async_client, user_token):
    """Test pagination of task list"""
    # Create multiple tasks
    for i in range(10):
        await async_client.post(
            "/api/v1/tasks",
            headers={"Authorization": f"Bearer {user_token}"},
            json={"title": f"Task {i}", "description": f"Description {i}", "due_date": "2023-10-15"}
        )
    
    # Fetch first page
    response = await async_client.get("/api/v1/tasks?page=1&limit=5", headers={"Authorization": f"Bearer {user_token}"})
    assert response.status_code == 200
    data = response.json()
    assert len(data["tasks"]) == 5

    # Fetch second page
    response = await async_client.get("/api/v1/tasks?page=2&limit=5", headers={"Authorization": f"Bearer {user_token}"})
    assert response.status_code == 200
    data = response.json()
    assert len(data["tasks"]) == 5