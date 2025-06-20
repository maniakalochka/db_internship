from __future__ import annotations
from .base import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey


class BuyBook(Base):
    __tablename__ = "buy_book"

    buy_book_id: Mapped[int] = mapped_column(primary_key=True)
    buy_id: Mapped[int] = mapped_column(ForeignKey("buy.buy_id"), nullable=False)
    book_id: Mapped[int] = mapped_column(ForeignKey("book.book_id"), nullable=False)
    amount: Mapped[int] = mapped_column(nullable=False)

    buy: Mapped["Buy"] = relationship(back_populates="buy_books")
    book: Mapped["Book"] = relationship(back_populates="buy_books")
