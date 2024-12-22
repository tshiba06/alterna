from abc import ABC, abstractmethod

from model import RakutenBank
from sqlalchemy.orm import Session


class Repository(ABC):
    @abstractmethod
    def create(self, session: Session,  bank: RakutenBank):
        pass


class RepositoryImpl(Repository):
    def create(self, session: Session, bank: RakutenBank):
        session.add(bank)
        session.commit()
