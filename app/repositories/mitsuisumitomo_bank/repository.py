from abc import ABC, abstractmethod
from typing import List

from sqlalchemy import desc
from sqlalchemy.orm import Session

from repositories.mitsuisumitomo_bank.model import MitsuisumitomoBank


class Repository(ABC):
    @abstractmethod
    def create(self, session: Session, bank: MitsuisumitomoBank):
        pass

    @abstractmethod
    def get_latest(self, session: Session) -> MitsuisumitomoBank | None:
        pass

    @abstractmethod
    def get_histories(self, session: Session) -> List[MitsuisumitomoBank]:
        pass


class RepositoryImpl(Repository):
    def create(self, session: Session, bank: MitsuisumitomoBank):
        session.add(bank)
        session.commit()

    def get_latest(self, session: Session) -> MitsuisumitomoBank | None:
        return (
            session.query(MitsuisumitomoBank)
            .order_by(desc(MitsuisumitomoBank.id))
            .limit(1)
            .one_or_none()
        )

    def get_histories(self, session) -> List[MitsuisumitomoBank]:
        return session.query(MitsuisumitomoBank).all()
