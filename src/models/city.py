from __future__ import annotations
from .base import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String



class City(Base):
    __tablename__ = "city"

    city_id: Mapped[int] = mapped_column(primary_key=True)
    name_city: Mapped[str] = mapped_column(String, nullable=False)
    days_delivery: Mapped[int] = mapped_column(nullable=False)

    clients: Mapped[list["Client"]] = relationship(back_populates="city")
