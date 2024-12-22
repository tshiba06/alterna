from model import CreateInput
from repositories.rakuten_bank.model import RakutenBank
from repositories.rakuten_bank.repository import Repository
from sqlalchemy.orm import Session


class UseCase:
    def __init__(self, session: Session, repository: Repository):
        self.session = session
        self.repository = repository

    def create(self, input: CreateInput):
        model = RakutenBank(total=input.total)
        try:
            self.repository.create(self.session, model)
        except Exception:
            print("insert error")
