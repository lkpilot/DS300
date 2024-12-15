from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy.ext.asyncio import async_sessionmaker
# Database connection string
DB_URL = "postgresql+asyncpg://postgres:luong11162003@localhost:5433/postgres"

# Create an async engine
engine = create_async_engine(DB_URL, pool_pre_ping=True, echo=True)

# Async session factory


# Async session factory
Session = async_sessionmaker(
    bind=engine,
    expire_on_commit=False,  # Prevent automatic detachment of instances
)

# Base class for ORM models
Base = declarative_base()