from __future__ import annotations

from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base


class Book(Base):
    __tablename__ = "book"

    book_id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String, nullable=False)
    author_id: Mapped[int] = mapped_column(
        ForeignKey("author.author_id"), nullable=False
    )
    genre_id: Mapped[int] = mapped_column(ForeignKey("genre.genre_id"), nullable=False)
    price: Mapped[int] = mapped_column(nullable=False)
    amount: Mapped[int] = mapped_column(nullable=False)

    author: Mapped["Author"] = relationship(back_populates="books")
    genre: Mapped["Genre"] = relationship(back_populates="books")
    buy_books: Mapped[list["BuyBook"]] = relationship(back_populates="book")
