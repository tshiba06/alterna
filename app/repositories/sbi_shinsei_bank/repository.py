from abc import ABC, abstractmethod
from typing import List

from sqlalchemy import desc
from sqlalchemy.orm import Session

from app.repositories.sbi_shinsei_bank.model import SbiShinseiBank # Corrected import


class Repository(ABC):
    @abstractmethod
    def create(self, session: Session, bank: SbiShinseiBank):
        pass

    @abstractmethod
    def get_latest(self, session: Session) -> SbiShinseiBank | None:
        pass

    @abstractmethod
    def get_histories(self, session: Session) -> List[SbiShinseiBank]:
        pass


class RepositoryImpl(Repository):
    def create(self, session: Session, bank: SbiShinseiBank):
        session.add(bank)
        session.commit()

    def get_latest(self, session: Session) -> SbiShinseiBank | None:
        return (
            session.query(SbiShinseiBank)
            .order_by(desc(SbiShinseiBank.id))
            .limit(1)
            .one_or_none()
        )

    def get_histories(self, session) -> List[SbiShinseiBank]:
        return session.query(SbiShinseiBank).all()
