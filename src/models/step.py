from __future__ import annotations

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base


class Step(Base):
    __tablename__ = "step"

    step_id: Mapped[int] = mapped_column(primary_key=True)
    name_step: Mapped[str] = mapped_column(String, nullable=False)

    buy_steps: Mapped[list["BuyStep"]] = relationship(back_populates="step")
