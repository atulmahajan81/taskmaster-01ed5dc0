from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy.orm import joinedload
from passlib.context import CryptContext
from backend.models import User
from backend.schemas import UserCreate
from uuid import uuid4

class UserService:
    """Service for user-related operations."""

    pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

    async def create_user(self, session: AsyncSession, user_create: UserCreate) -> User:
        """Create a new user."""
        hashed_password = self.pwd_context.hash(user_create.password)
        user = User(id=uuid4(), email=user_create.email, hashed_password=hashed_password)
        session.add(user)
        await session.commit()
        await session.refresh(user)
        return user

    async def authenticate_user(self, session: AsyncSession, email: str, password: str) -> User:
        """Authenticate a user."""
        result = await session.execute(select(User).options(joinedload(User.tasks)).where(User.email == email))
        user = result.scalars().first()
        if user and self.pwd_context.verify(password, user.hashed_password):
            return user
        return None