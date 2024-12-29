from repositories.sbi_benefit_system.model import SbiBenefitSystem
from repositories.sbi_benefit_system.repository import Repository
from services.sbi_benefit_system.service import Service as SService
from sqlalchemy.orm import Session

from use_cases.sbi_benefit_system.model import GetHistoriesOutput, GetHistoryOutput


class UseCase:
    def __init__(self, session: Session, scraping_service: SService, repository: Repository):
        self.session = session
        self.repository = repository
        self.scraping_service = scraping_service

    async def create(self) -> int:
        total = await self.scraping_service.run()
        if total < 0:
            return 500

        try:
            model = SbiBenefitSystem(total=total)
            self.repository.create(self.session, model)

            return 200
        except Exception as e:
            print("insert error: ", e)
            return 500

    def get_latest(self) -> int:
        sbi_benefit_system = self.repository.get_latest(session=self.session)

        if sbi_benefit_system is not None:
            return sbi_benefit_system.total
        else:
            return 0

    def get_histories(self) -> GetHistoriesOutput:
        sbi_benefit_systems = self.repository.get_histories(session=self.session)

        result = [
            GetHistoryOutput(created_at=s.created_at, total=s.total)
            for s in sbi_benefit_systems
        ]

        return GetHistoriesOutput(result)
