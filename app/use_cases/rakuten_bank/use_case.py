from repositories.rakuten_bank.model import RakutenBank
from repositories.rakuten_bank.repository import Repository
from services.rakuten_bank.service import Service as SService
from sqlalchemy.orm import Session


class UseCase:
    def __init__(
        self, session: Session, scraping_service: SService, repository: Repository
    ):
        self.session = session
        self.repository = repository
        self.scraping_service = scraping_service

    async def create(self) -> int:
        total = await self.scraping_service.run()
        if total < 0:
            return 500

        try:
            model = RakutenBank(total=total)
            self.repository.create(self.session, model)

            return 200
        except Exception as e:
            print("insert error: ", e)
            return 500

    def get_latest(self) -> int:
        rakuten_bank = self.repository.get_latest(session=self.session)

        if rakuten_bank is not None:
            return rakuten_bank.total
        else:
            return 0
