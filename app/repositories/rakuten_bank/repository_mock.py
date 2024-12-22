from sqlalchemy.orm import Session

from repositories.rakuten_bank.model import RakutenBank
from repositories.rakuten_bank.repository import Repository


class RepositoryMock(Repository):
    create_call_counts = 0
    create_call_args = []

    def create(self, session: Session, bank: RakutenBank):
        self.create_call_counts += 1
        self.create_call_args.append(bank)
