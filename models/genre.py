from __future__ import annotations
from .base import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String
from book import Book

class Genre(Base):
    __tablename__ = "genre"

    genre_id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name_genre: Mapped[str] = mapped_column(String, unique=True, nullable=False)

    books: Mapped[list["Book"]] = relationship(back_populates="genre")

    def __repr__(self) -> str:
        return f"<Genre(id={self.genre_id}, name='{self.name_genre}')>"
