from repositories.rakuten_bank.model import RakutenBank
from repositories.rakuten_bank.repository import Repository
from services.rakuten_bank.service import Service as SService
from sqlalchemy.orm import Session


class UseCase:
    def __init__(self, session: Session, scraping_service: SService, repository: Repository):
        self.session = session
        self.repository = repository
        self.scraping_service = scraping_service

    def create(self):
        total = self.scraping_service.run()
        print(total)

        try:
            model = RakutenBank(total=total)
            self.repository.create(self.session, model)
        except Exception:
            print("insert error")
