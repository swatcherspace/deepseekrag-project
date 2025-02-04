import sys
import os

# Add the app directory to the sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../app')))

from fastapi.testclient import TestClient
from app.main import app  # Import your FastAPI app
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from app.database import Base, get_db
import pytest

# Configure test database
DATABASE_URL = "postgresql+asyncpg://postgres:abhishek1234@localhost/rag_db"

engine = create_engine(DATABASE_URL)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create tables for testing
Base.metadata.create_all(engine)

# Override get_db dependency
def get_test_db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()

client = TestClient(app)

# Add your test cases here
def test_qna_valid_query():
    response = client.post(
        "/api/qna/",
        json={"query": "What is AI?"}
    )
    assert response.status_code == 200
    assert "answer" in response.json()