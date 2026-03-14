from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.gzip import GZipMiddleware
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import declarative_base
from sqlalchemy.ext.asyncio import async_sessionmaker
from contextlib import asynccontextmanager
from backend.routers import auth as auth_router, users as users_router
from backend.routers import task as resource_router

DATABASE_URL = "postgresql+asyncpg://user:password@localhost/taskmaster"

engine = create_async_engine(DATABASE_URL, echo=False)  # Ensure echo is False in production
AsyncSessionLocal = async_sessionmaker(bind=engine, expire_on_commit=False)
Base = declarative_base()

@asynccontextmanager
def lifespan(app: FastAPI):
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield

app = FastAPI(lifespan=lifespan)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[  # Restrict in production
        "http://localhost",
        "http://localhost:3000",
        "http://localhost:8000"
    ],
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],  # Restrict m
)

app.add_middleware(GZipMiddleware, minimum_size=1000)