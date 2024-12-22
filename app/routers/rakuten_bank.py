from use_cases.rakuten_bank.use_case import UseCase

from routers.router import Router


class RakutenBankRouter(Router):
    def __init__(self, use_case: UseCase):
        self.use_case = use_case

    async def get_latest(self):
        pass

    async def save(self):
        pass

    async def get_history(self):
        pass
