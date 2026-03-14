from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from pydantic import EmailStr, validator
from backend.models import User
from backend.schemas import UserCreate, UserOut, TokenOut
from backend.auth import verify_password, get_password_hash, create_access_token, create_refresh_token
from backend.dependencies import oauth2_scheme
from backend.tasks import send_email_task  # Email sending moved to Celery

router = APIRouter(prefix="/api/v1/auth", tags=["auth"])

# Add validation for input length and format

@router.post("/register", response_model=UserOut)
async def register(user_create: UserCreate, db: AsyncSession = Depends()):
    if len(user_create.password) < 8 or not any(char.isdigit() for char in user_create.password) or not any(char.isupper() for char in user_create.password):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Password too weak. Must be at least 8 characters, include a number and an uppercase letter.")
    if not isinstance(user_create.email, EmailStr):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid email format")
    async with db.b