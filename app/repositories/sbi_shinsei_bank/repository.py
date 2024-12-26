from abc import ABC, abstractmethod

from sqlalchemy.orm import Session

from repositories.sbi_shinsei_bank.model import SbiShinseiBank


class Repository(ABC):
    @abstractmethod
    def create(self, session: Session, bank: SbiShinseiBank):
        pass



class RepositoryImpl(Repository):
    def create(self, session: Session, bank: SbiShinseiBank):
        session.add(bank)
        session.commit()
