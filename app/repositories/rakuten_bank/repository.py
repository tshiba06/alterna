from abc import ABC, abstractmethod

from sqlalchemy import desc
from sqlalchemy.orm import Session

from repositories.rakuten_bank.model import RakutenBank


class Repository(ABC):
    @abstractmethod
    def create(self, session: Session, bank: RakutenBank):
        pass

    @abstractmethod
    def get_latest(self, session: Session) -> RakutenBank | None:
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
