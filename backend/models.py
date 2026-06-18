from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Float
from sqlalchemy import Boolean
from sqlalchemy import DateTime

from datetime import datetime

from backend.database import Base

class QueryLog(Base):

    __tablename__ = "query_logs"

    id = Column(Integer, primary_key=True)

    question = Column(String)

    answer = Column(String)

    source = Column(String)

    response_time = Column(Float)

    answer_found = Column(Boolean)

    created_at = Column(DateTime, default=datetime.utcnow)