from __future__ import annotations

from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base


class Buy(Base):
    __tablename__ = "buy"

    buy_id: Mapped[int] = mapped_column(primary_key=True)
    buy_description: Mapped[str] = mapped_column(String, nullable=False)
    client_id: Mapped[int] = mapped_column(
        ForeignKey("client.client_id"), nullable=False
    )

    client: Mapped["Client"] = relationship(back_populates="buys")
    buy_books: Mapped[list["BuyBook"]] = relationship(back_populates="buy")
    buy_steps: Mapped[list["BuyStep"]] = relationship(back_populates="buy")
