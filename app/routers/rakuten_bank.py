from fastapi import status
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from internal.log import logger
from use_cases.rakuten_bank.use_case import UseCase

from routers.router import Router


class RakutenBankRouter(Router):
    def __init__(self, use_case: UseCase):
        super().__init__(prefix="/banks/rakuten")
        self.use_case = use_case

    def get_latest(self):
        total = self.use_case.get_latest()

        return JSONResponse(content={"total": total}, status_code=status.HTTP_200_OK)

    async def save(self):
        logger.info("save rakuten")
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

    def get_history(self):
        result = self.use_case.get_histories()

        return JSONResponse(
            content={"histories": jsonable_encoder(result)},
            status_code=status.HTTP_200_OK,
        )
