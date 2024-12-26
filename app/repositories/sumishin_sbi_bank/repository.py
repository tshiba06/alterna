from abc import ABC, abstractmethod

from sqlalchemy.orm import Session

from repositories.sumishin_sbi_bank.model import SumishinSbiBank


class Repository(ABC):
    @abstractmethod
    def create(self, session: Session, bank: SumishinSbiBank):
        pass


class RepositoryImpl(Repository):
    def create(self, session: Session, bank: SumishinSbiBank):
        session.add(bank)
        session.commit()
