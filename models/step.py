from __future__ import annotations
from .base import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String

from buy_step import BuyStep

class Step(Base):
    __tablename__ = "step"

    step_id: Mapped[int] = mapped_column(primary_key=True)
    name_step: Mapped[str] = mapped_column(String, nullable=False)

    buy_steps: Mapped[list[BuyStep]] = relationship(back_populates="step")
