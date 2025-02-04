from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from pydantic import BaseModel
from app.database import get_db
from app.models import Document
from app.services.embedding import generate_embedding

router = APIRouter()

# Define the expected request format
class DocumentRequest(BaseModel):
    title: str
    content: str

@router.post("/ingest/")
async def ingest_document(doc: DocumentRequest, db: AsyncSession = Depends(get_db)):
    embedding = generate_embedding(doc.content)
    new_doc = Document(title=doc.title, content=doc.content, embeddings=embedding)
    db.add(new_doc)
    await db.commit()
    return {"message": "Document stored successfully"}
