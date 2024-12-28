from repositories.sbi_shinsei_bank.model import SbiShinseiBank
from repositories.sbi_shinsei_bank.repository import Repository
from services.sbi_shinsei_bank.service import Service as SService
from sqlalchemy.orm import Session

from use_cases.sbi_shinsei_bank.model import GetHistoriesOutput, GetHistoryOutput


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
            model = SbiShinseiBank(total=total)
            self.repository.create(self.session, model)

            return 200
        except Exception as e:
            print("insert error: ", e)
            return 500

    def get_latest(self) -> int:
        sbi_shinsei_bank = self.repository.get_latest(session=self.session)

        if sbi_shinsei_bank is not None:
            return sbi_shinsei_bank.total
        else:
            return 0

    def get_histories(self) -> GetHistoriesOutput:
        sbi_shinsei_banks = self.repository.get_histories(session=self.session)

        result = [
            GetHistoryOutput(created_at=s.created_at, total=s.total)
            for s in sbi_shinsei_banks
        ]

        return GetHistoriesOutput(result)
