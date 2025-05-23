from sqlalchemy.orm import Session

from app.repositories.mitsuisumitomo_card.model import MitsuisumitomoCard
from app.repositories.mitsuisumitomo_card.repository import (
    Repository as SMCCardRepository,
)
from app.services.mitsuisumitomo_card.service import (
    ServiceImpl as SMCCardScrapingService,
)
from app.use_cases.mitsuisumitomo_card.model import (
    GetHistoriesOutput,
    GetHistoryOutput,
)


class UseCase:
    def __init__(
        self,
        db_session: Session,
        smc_card_repository: SMCCardRepository,
        smc_card_scraping_service: SMCCardScrapingService,
    ):
        self.db_session = db_session
        self.smc_card_repository = smc_card_repository
        self.smc_card_scraping_service = smc_card_scraping_service

    async def create_history(self) -> int:
        try:
            # Assuming run() returns the total amount or raises an exception
            total_amount = await self.smc_card_scraping_service.run()

            card_info = MitsuisumitomoCard(total=total_amount)
            self.smc_card_repository.create(self.db_session, card_info)
            self.db_session.commit()  # Commit here for this simple use case
            return 200  # Indicate success
        except Exception as e:
            # Log the exception e
            self.db_session.rollback()
            return 500  # Indicate failure

    def get_latest_total(self) -> int | None:
        latest_info = self.smc_card_repository.get_latest(self.db_session)
        if latest_info:
            return latest_info.total
        return None

    def get_histories(self) -> GetHistoriesOutput:
        card_histories = self.smc_card_repository.get_histories(self.db_session)
        result = [
            GetHistoryOutput.model_validate(h) for h in card_histories
        ] # Use model_validate for Pydantic v2
        return GetHistoriesOutput(histories=result)
