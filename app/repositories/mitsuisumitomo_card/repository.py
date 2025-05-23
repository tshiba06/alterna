from abc import ABC, abstractmethod
from typing import List

from sqlalchemy import desc
from sqlalchemy.orm import Session

from app.repositories.mitsuisumitomo_card.model import MitsuisumitomoCard


class Repository(ABC):
    @abstractmethod
    def create(self, session: Session, card_info: MitsuisumitomoCard) -> MitsuisumitomoCard:
        pass

    @abstractmethod
    def get_latest(self, session: Session) -> MitsuisumitomoCard | None:
        pass

    @abstractmethod
    def get_histories(self, session: Session) -> List[MitsuisumitomoCard]:
        pass


class RepositoryImpl(Repository):
    def create(self, session: Session, card_info: MitsuisumitomoCard) -> MitsuisumitomoCard:
        session.add(card_info)
        # session.commit() # Commit should be handled by the use case or a unit of work
        return card_info

    def get_latest(self, session: Session) -> MitsuisumitomoCard | None:
        return (
            session.query(MitsuisumitomoCard)
            .order_by(desc(MitsuisumitomoCard.created_at)) # Order by created_at
            .limit(1)
            .one_or_none()
        )

    def get_histories(self, session: Session) -> List[MitsuisumitomoCard]:
        return (
            session.query(MitsuisumitomoCard)
            .order_by(desc(MitsuisumitomoCard.created_at)) # Order by created_at
            .all()
        )
