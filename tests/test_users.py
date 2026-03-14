# test_users.py

import pytest

@pytest.mark.asyncio
async def test_get_user_details(async_client, user_token):
    """Test retrieving user details with valid token"""
    response = await async_client.get("/api/v1/users/me", headers={"Authorization": f"Bearer {user_token}"})
    assert response.status_code == 200
    data = response.json()
    assert "user_id" in data
    assert "email" in data

@pytest.mark.asyncio
async def test_update_user_details(async_client, user_token):
    """Test updating user details with valid data"""
    response = await async_client.put(
        "/api/v1/users/me", 
        headers={"Authorization": f"Bearer {user_token}"},
        json={"email": "new_email@test.com"}
    )
    assert response.status_code == 200
    data = response.json()
    assert data["email"] == "new_email@test.com"

@pytest.mark.asyncio
async def test_delete_user(async_client, user_token):
    """Test deleting user account"""
    response = await async_client.delete("/api/v1/users/me", headers={"Authorization": f"Bearer {user_token}"})
    assert response.status_code == 200
    data = response.json()
    assert data["message"] == "User deleted successfully"