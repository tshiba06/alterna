from internal.log import logger
from use_cases.rakuten_bank.use_case import UseCase

from routers.router import Router


class RakutenBankRouter(Router):
    def __init__(self, use_case: UseCase):
        super().__init__(prefix="/banks/rakuten")
        self.use_case = use_case

    async def get_latest(self):
        pass

    def save(self):
        logger.info("head save")
        try:
            self.use_case.create()
        except Exception as e:
            print(e)
            print("exception")

    async def get_history(self):
        pass
