from abc import ABC, abstractmethod

from sqlalchemy.orm import Session

from repositories.rakuten_bank.model import RakutenBank


class Repository(ABC):
    @abstractmethod
    def create(self, session: Session,  bank: RakutenBank):
        pass


class RepositoryImpl(Repository):
    def create(self, session: Session, bank: RakutenBank):
        session.add(bank)
        session.commit()
