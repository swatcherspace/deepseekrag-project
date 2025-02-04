import sys
import os

# Add the app directory to the sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../app')))

from app.main import app

from fastapi.testclient import TestClient
from main import app
from sqlalchemy.ext.asyncio import AsyncSession
from app.database import Base, get_db
from app.models import Document
import pytest

client = TestClient(app)

def test_ingest_valid_document():
    doc_data = {"title": "Test Document", "content": "This is a test."}
    response = client.post("/api/ingest/", json=doc_data)
    assert response.status_code == 200
    assert response.json()["message"] == "Document stored successfully"

    # Verify document is stored in the database
    db = next(get_test_db())
    stored_doc = db.query(Document).filter_by(title="Test Document").first()
    assert stored_doc is not None
    assert stored_doc.content == "This is a test."