from abc import ABC, abstractmethod
from typing import List

from sqlalchemy import desc
from sqlalchemy.orm import Session

from app.repositories.sumishin_sbi_bank.model import SumishinSbiBank # Corrected import


class Repository(ABC):
    @abstractmethod
    def create(self, session: Session, bank: SumishinSbiBank):
        pass

    @abstractmethod
    def get_latest(self, session: Session) -> SumishinSbiBank | None:
        pass

    @abstractmethod
    def get_histories(self, session: Session) -> List[SumishinSbiBank]:
        pass


class RepositoryImpl(Repository):
    def create(self, session: Session, bank: SumishinSbiBank):
        session.add(bank)
        session.commit()

    def get_latest(self, session: Session) -> SumishinSbiBank | None:
        return (
            session.query(SumishinSbiBank)
            .order_by(desc(SumishinSbiBank.id))
            .limit(1)
            .one_or_none()
        )

    def get_histories(self, session) -> List[SumishinSbiBank]:
        return session.query(SumishinSbiBank).all()
