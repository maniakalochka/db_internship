from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


from models.author import Author
from models.book import Book
from models.buy import Buy
from models.buy_book import BuyBook
from models.buy_step import BuyStep
from models.city import City
from models.client import Client
from models.genre import Genre
from models.step import Step

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
