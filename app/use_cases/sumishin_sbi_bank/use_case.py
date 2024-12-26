from repositories.sumishin_sbi_bank.model import SumishinSbiBank
from repositories.sumishin_sbi_bank.repository import Repository
from services.sumishin_sbi_bank.service import Service as SService
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
            model = SumishinSbiBank(total=total)
            self.repository.create(self.session, model)

            return 200
        except Exception as e:
            print("insert error: ", e)
            return 500
