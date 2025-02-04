from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker
from app.models import Base
import asyncio
import os

DATABASE_URL = os.getenv("DATABASE_URL", "postgresql+asyncpg://postgres:abhishek1234@localhost/rag_db")

engine = create_async_engine(DATABASE_URL, echo=True)
AsyncSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine, class_=AsyncSession)

async def init_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)  # Create tables

async def get_db():
    async with AsyncSessionLocal() as session:
        yield session

# Run the database initialization when starting the application
if __name__ == "__main__":
    asyncio.run(init_db())
