from routers.router import Router


class MitsuisumitomoBankRouter(Router):
    def __init__(self):
        super().__init__(prefix="/banks/mitsuisumitomo")

    async def get_latest(self):
        pass

    async def save(self):
        pass

    async def get_history(self):
        pass
