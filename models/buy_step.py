from __future__ import annotations
from datetime import date as Date
from .base import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey

from buy import Buy
from step import Step

class BuyStep(Base):
    __tablename__ = "buy_step"

    buy_step_id: Mapped[int] = mapped_column(primary_key=True)
    buy_id: Mapped[int] = mapped_column(ForeignKey("buy.buy_id"), nullable=False)
    step_id: Mapped[int] = mapped_column(ForeignKey("step.step_id"), nullable=False)
    date_step_beg: Mapped[Date] = mapped_column(nullable=False)
    date_step_end: Mapped[Date] = mapped_column(nullable=True)

    buy: Mapped[Buy] = relationship(back_populates="buy_steps")
    step: Mapped[Step] = relationship(back_populates="buy_steps")
