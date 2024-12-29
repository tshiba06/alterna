from datetime import datetime

from sqlalchemy import TIMESTAMP, Column, Integer

from repositories.model import Base


class SbiBenefitSystem(Base):
    __tablename__ = "sbi_benefit_systems"

    id = Column(Integer, primary_key=True)
    total = Column(Integer, comment="残高")
    created_at = Column(TIMESTAMP, default=datetime.now)
