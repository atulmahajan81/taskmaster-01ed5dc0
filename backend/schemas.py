from datetime import datetime
from uuid import UUID
from pydantic import BaseModel, EmailStr, ConfigDict

class UserBase(BaseModel):
    email: EmailStr

    model_config = ConfigDict(from_attributes=True)

class UserCreate(UserBase):
    password: str

class UserOut(UserBase):
    id: UUID
    created_at: datetime

class TaskBase(BaseModel):
    title: str
    description: str | None = None
    due_date: datetime | None = None
    priority: str | None = None
    status: str = 'pending'

    model_config = ConfigDict(from_attributes=True)

class TaskCreate(TaskBase):
    pass

class TaskUpdate(BaseModel):
    title: str | None = None
    description: str | None = None
    due_date: datetime | None = None
    priority: str | None = None
    status: str | None = None

class TaskOut(TaskBase):
    id: UUID
    user_id: UUID
    created_at: datetime
    updated_at: datetime

class NotificationBase(BaseModel):
    message: str
    read: bool = False

    model_config = ConfigDict(from_attributes=True)

class NotificationCreate(NotificationBase):
    pass

class NotificationUpdate(BaseModel):
    message: str | None = None
    read: bool | None = None

class NotificationOut(NotificationBase):
    id: UUID
    user_id: UUID
    created_at: datetime
    updated_at: datetime

class TokenOut(BaseModel):
    access_token: str
    token_type: str = 'bearer'