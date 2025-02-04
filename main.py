from fastapi import FastAPI
from app.routes import ingestion, qna

app = FastAPI()

app.include_router(ingestion.router, prefix="/api")
app.include_router(qna.router, prefix="/api")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
