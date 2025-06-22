from __future__ import annotations

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base


class City(Base):
    __tablename__ = "city"

    city_id: Mapped[int] = mapped_column(primary_key=True)
    name_city: Mapped[str] = mapped_column(String, nullable=False)
    days_delivery: Mapped[int] = mapped_column(nullable=False)

    clients: Mapped[list["Client"]] = relationship(back_populates="city")
