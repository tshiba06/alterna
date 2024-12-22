from dataclasses import dataclass
from datetime import datetime

from sqlalchemy import TIMESTAMP, Column, Integer

from repositories.model import Base


@dataclass
class RakutenBank(Base):
    __table__name = "rakuten_banks"

    id = Column(Integer, primary_key=True)
    total = Column(Integer, comment="残高")
    created_at = Column(TIMESTAMP, default=datetime.now)
