from sqlalchemy import Column, DateTime, Integer
from sqlalchemy.sql import func

from app.repositories.model import Base # Corrected import


class MitsuisumitomoCard(Base):
    __tablename__ = "mitsuisumitomo_cards"

    id = Column(Integer, primary_key=True, autoincrement=True)
    total = Column(Integer, nullable=False)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())

    def __repr__(self):
        return f"<MitsuisumitomoCard(id={self.id}, total={self.total})>"
