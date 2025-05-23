from abc import ABC, abstractmethod
from typing import List

from sqlalchemy import desc
from sqlalchemy.orm import Session

from app.repositories.rakuten_bank.model import RakutenBank # Corrected import


class Repository(ABC):
    @abstractmethod
    def create(self, session: Session, bank: RakutenBank):
        pass

    @abstractmethod
    def get_latest(self, session: Session) -> RakutenBank | None:
        pass

    @abstractmethod
    def get_histories(self, session: Session) -> List[RakutenBank]:
        pass


class RepositoryImpl(Repository):
    def create(self, session: Session, bank: RakutenBank):
        session.add(bank)
        session.commit()

    def get_latest(self, session: Session) -> RakutenBank | None:
        return (
            session.query(RakutenBank)
            .order_by(desc(RakutenBank.id))
            .limit(1)
            .one_or_none()
        )

    def get_histories(self, session) -> List[RakutenBank]:
        return session.query(RakutenBank).all()
