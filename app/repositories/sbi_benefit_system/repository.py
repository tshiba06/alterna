from abc import ABC, abstractmethod
from typing import List

from sqlalchemy import desc
from sqlalchemy.orm import Session

from app.repositories.sbi_benefit_system.model import SbiBenefitSystem # Corrected import


class Repository(ABC):
    @abstractmethod
    def create(self, session: Session, bank: SbiBenefitSystem):
        pass

    @abstractmethod
    def get_latest(self, session: Session) -> SbiBenefitSystem | None:
        pass

    @abstractmethod
    def get_histories(self, session: Session) -> List[SbiBenefitSystem]:
        pass


class RepositoryImpl(Repository):
    def create(self, session: Session, bank: SbiBenefitSystem):
        session.add(bank)
        session.commit()

    def get_latest(self, session: Session) -> SbiBenefitSystem | None:
        return (
            session.query(SbiBenefitSystem)
            .order_by(desc(SbiBenefitSystem.id))
            .limit(1)
            .one_or_none()
        )

    def get_histories(self, session) -> List[SbiBenefitSystem]:
        return session.query(SbiBenefitSystem).all()
