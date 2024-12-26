from fastapi import status
from fastapi.responses import JSONResponse
from internal.log import logger
from use_cases.rakuten_bank.use_case import UseCase

from routers.router import Router


class RakutenBankRouter(Router):
    def __init__(self, use_case: UseCase):
        super().__init__(prefix="/banks/rakuten")
        self.use_case = use_case

    async def get_latest(self):
        pass

    async def save(self):
        logger.info("head save")
        try:
            result = await self.use_case.create()

            if result == 200:
                return JSONResponse(
                    content={"message": "success"}, status_code=status.HTTP_200_OK
                )
            else:
                return JSONResponse(
                    content={"message": "failed"},
                    status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                )
        except Exception as e:
            print(e)
            return JSONResponse(
                content={"message": "failed"},
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )

    async def get_history(self):
        pass
