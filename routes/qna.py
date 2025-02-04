from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.database import get_db
from app.models import Document
from app.services.retrieval import get_relevant_docs, generate_answer

router = APIRouter()
from pydantic import BaseModel

class QuestionRequest(BaseModel):
    query: str
@router.post("/qna/")
async def ask_question(request: QuestionRequest, db: AsyncSession = Depends(get_db)):
    docs = await get_relevant_docs(request.query, db)
    answer = generate_answer(request.query, docs)
    return {"answer": answer}
