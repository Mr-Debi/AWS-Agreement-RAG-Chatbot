from sqlalchemy import func
from backend.models import QueryLog


def get_analytics(db):

    top_questions = (
        db.query(
            QueryLog.question,
            func.count(QueryLog.id)
        )
        .group_by(QueryLog.question)
        .all()
    )

    avg_latency = (
        db.query(
            func.avg(QueryLog.response_time)
        )
        .scalar()
    )

    no_answer = (
        db.query(QueryLog.question)
        .filter(QueryLog.answer_found == False)
        .all()
    )

    return {
        "top_questions": [
            {
                "question": q,
                "count": c
            }
            for q, c in top_questions
        ],
        "avg_latency": float(avg_latency) if avg_latency else 0,
        "no_answer_queries": [
            q[0]
            for q in no_answer
        ]
    }