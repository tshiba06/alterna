from repositories.mitsuisumitomo_bank.model import MitsuisumitomoBank
from repositories.mitsuisumitomo_bank.repository import Repository as MBRepository
from selenium.webdriver import Chrome
from services.mitsuisumitomo_bank.service import ServiceImpl as MBService
from sqlalchemy.orm import Session


class UseCase:
    def __init__(self, session: Session, repository: MBRepository, scraping_service: MBService):
        self.session = session
        self.repository = repository
        self.scraping_service = scraping_service

    async def first_authentication(self, driver: Chrome) -> str | None:
        result = await self.scraping_service.initial_run(driver=driver)

        if result:
            return result
        else:
            return None

    async def second_authentication(self, driver: Chrome):
        result = await self.scraping_service.second_run(driver=driver)
        if result:
            model = MitsuisumitomoBank(total=result)
            self.repository.create(session=self.session, bank=model)
            return 200
        else:
            return 500
