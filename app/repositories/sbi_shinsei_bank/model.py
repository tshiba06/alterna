from datetime import datetime

from sqlalchemy import TIMESTAMP, Column, Integer

from app.repositories.model import Base # Ensured single correct import


class SbiShinseiBank(Base):
    __tablename__ = "sbi_shinsei_banks"

    id = Column(Integer, primary_key=True)
    total = Column(Integer, comment="残高")
    created_at = Column(TIMESTAMP, default=datetime.now)
