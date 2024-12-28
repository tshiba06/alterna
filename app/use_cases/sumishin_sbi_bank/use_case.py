from repositories.sumishin_sbi_bank.model import SumishinSbiBank
from repositories.sumishin_sbi_bank.repository import Repository
from services.sumishin_sbi_bank.service import Service as SService
from sqlalchemy.orm import Session

from use_cases.sumishin_sbi_bank.model import GetHistoriesOutput, GetHistoryOutput


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

    def get_latest(self) -> int:
        sumishin_sbi_bank = self.repository.get_latest(session=self.session)

        if sumishin_sbi_bank is not None:
            return sumishin_sbi_bank.total
        else:
            return 0

    def get_histories(self) -> GetHistoriesOutput:
        rakuten_banks = self.repository.get_histories(session=self.session)

        result = [
            GetHistoryOutput(created_at=r.created_at, total=r.total)
            for r in rakuten_banks
        ]

        return GetHistoriesOutput(result)
