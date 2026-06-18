import time

from fastapi import FastAPI
from pydantic import BaseModel

from backend.database import Base
from backend.database import engine
from backend.database import SessionLocal

from backend.models import QueryLog
from backend.rag import ingest_pdf
from backend.rag import ask_question
from backend.analytics import get_analytics

Base.metadata.create_all(bind=engine)

app = FastAPI()


class Question(BaseModel):
    query: str


@app.post("/ingest")
def ingest():

    chunks = ingest_pdf(
        "backend/aws_customer_agreement.pdf"
    )

    return {
        "chunks_created": chunks
    }


@app.post("/ask")
def ask(data: Question):

    start = time.time()

    result = ask_question(
        data.query
    )

    latency = time.time() - start

    found = (
        "Information not found"
        not in result["answer"]
    )

    db = SessionLocal()

    log = QueryLog(
        question=data.query,
        answer=result["answer"],
        source=str(result["sources"]),
        response_time=latency,
        answer_found=found
    )

    db.add(log)

    db.commit()

    db.close()

    return result


@app.get("/analytics")
def analytics():

    db = SessionLocal()

    result = get_analytics(db)

    db.close()

    return result