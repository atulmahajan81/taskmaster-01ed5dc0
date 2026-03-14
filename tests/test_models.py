# test_models.py

import pytest
from sqlalchemy.exc import IntegrityError
from backend.models import User, Task

@pytest.mark.asyncio
async def test_user_model_constraints(test_db):
    """Test user model unique email constraint"""
    async with test_db() as db:
        user = User(email="unique@test.com", password_hash="hashedpassword")
        db.add(user)
        await db.commit()

        # Attempt to add another user with the same email
        another_user = User(email="unique@test.com", password_hash="anotherhash")
        db.add(another_user)
        with pytest.raises(IntegrityError):
            await db.commit()

@pytest.mark.asyncio
async def test_task_model_relationship(test_db):
    """Test task model foreign key constraint"""
    async with test_db() as db:
        invalid_task = Task(user_id="nonexistent-user", title="Title", description="Description")
        db.add(invalid_task)
        with pytest.raises(IntegrityError):
            await db.commit()