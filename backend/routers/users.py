from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from backend.models import User
from backend.schemas import UserOut, UserUpdate
from backend.dependencies import get_current_user
from typing import Optional

router = APIRouter(prefix="/api/v1/users", tags=["users"])

@router.get("/", response_model=list[UserOut])
async def list_users(cursor: Optional[str] = None, limit: int = 10, db: AsyncSession = Depends()):
    async with db.begin():
        query = select(User)
        if cursor:
            query = query.where(User.id > cursor)
        result = await db.execute(query.limit(limit))
        users = result.scalars().all()
        return [UserOut.from_orm(user) for user in users]

@router.get("/{id}", response_model=UserOut)
async def get_user(id: str, db: AsyncSession = Depends()):
    async with db.begin():
        result = await db.execute(select(User).where(User.id == id))
        user = result.scalars().first()
        if user is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
        return UserOut.from_orm(user)