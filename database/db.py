from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.base import Base

from core.config import settings


engine = create_engine(
    url=settings.DB_URL,
    echo=True,
    pool_pre_ping=True,
)
# Session Factory
SessionLocal = sessionmaker(autocommit=False, autoflush=True, bind=engine)

def init_db() -> None:
    Base.metadata.create_all(bind=engine)
