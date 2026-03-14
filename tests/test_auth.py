# test_auth.py

import pytest

@pytest.mark.asyncio
async def test_register_user(async_client):
    """Test user registration with valid data"""
    response = await async_client.post("/api/v1/auth/register", json={"email": "test@example.com", "password": "securepassword"})
    assert response.status_code == 201
    data = response.json()
    assert "user_id" in data
    assert data["email"] == "test@example.com"

@pytest.mark.asyncio
async def test_register_user_invalid_data(async_client):
    """Test registration with missing password"""
    response = await async_client.post("/api/v1/auth/register", json={"email": "test@example.com"})
    assert response.status_code == 422

@pytest.mark.asyncio
async def test_login_user(async_client):
    """Test user login with correct credentials"""
    await async_client.post("/api/v1/auth/register", json={"email": "login@test.com", "password": "password123"})
    response = await async_client.post("/api/v1/auth/login", json={"email": "login@test.com", "password": "password123"})
    assert response.status_code == 200
    data = response.json()
    assert "access_token" in data
    assert "refresh_token" in data

@pytest.mark.asyncio
async def test_login_invalid_credentials(async_client):
    """Test login with invalid credentials"""
    response = await async_client.post("/api/v1/auth/login", json={"email": "wrong@test.com", "password": "wrongpass"})
    assert response.status_code == 401

@pytest.mark.asyncio
async def test_token_refresh(async_client, user_token):
    """Test token refresh with valid refresh token"""
    response = await async_client.post("/api/v1/auth/refresh", headers={"Authorization": f"Bearer {user_token}"}, json={"refresh_token": "valid_refresh_token"})
    assert response.status_code == 200
    data = response.json()
    assert "access_token" in data

@pytest.mark.asyncio
async def test_logout(async_client, user_token):
    """Test user logout"""
    response = await async_client.post("/api/v1/auth/logout", headers={"Authorization": f"Bearer {user_token}"})
    assert response.status_code == 200
    data = response.json()
    assert data["message"] == "Successfully logged out"