from __future__ import annotations

from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base


class Client(Base):
    __tablename__ = "client"

    client_id: Mapped[int] = mapped_column(primary_key=True)
    name_client: Mapped[str] = mapped_column(String, nullable=False)
    city_id: Mapped[int] = mapped_column(ForeignKey("city.city_id"), nullable=False)
    email: Mapped[str] = mapped_column(String, nullable=False)

    city: Mapped["City"] = relationship(back_populates="clients")
    buys: Mapped[list["Buy"]] = relationship(back_populates="client")
