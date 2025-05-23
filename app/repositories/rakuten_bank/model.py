from datetime import datetime

from sqlalchemy import TIMESTAMP, Column, Integer

from app.repositories.model import Base # Ensured single correct import


class RakutenBank(Base):
    __tablename__ = "rakuten_banks"

    id = Column(Integer, primary_key=True)
    total = Column(Integer, comment="残高")
    created_at = Column(TIMESTAMP, default=datetime.now)
