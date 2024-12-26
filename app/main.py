from db.db import session
from dotenv import load_dotenv
from fastapi import FastAPI
from repositories.rakuten_bank.repository import RepositoryImpl as RakutenRepository
from repositories.sbi_shinsei_bank.repository import (
    RepositoryImpl as SbiShinseiRepository,
)
from routers.mitsuisumitomo_bank import MitsuisumitomoBankRouter
from routers.rakuten_bank import RakutenBankRouter
from routers.sbi_shinsei_bank import SbiShinseiBankRouter
from routers.sumishin_sbi_bank import SumishinSbiBankRouter
from services.rakuten_bank.service import ServiceImpl as RakutenScrapingService
from services.sbi_shinsei_bank.service import ServiceImpl as SbiShinseiScrapingService
from use_cases.rakuten_bank.use_case import UseCase as RakutenUseCase
from use_cases.sbi_shinsei_bank.use_case import UseCase as SbiShinseiUseCase

load_dotenv()

app = FastAPI()

# repositories
rakuten_repository = RakutenRepository()
sbi_shinsei_repository = SbiShinseiRepository()


# services
rakuten_scraping_service = RakutenScrapingService()
sbi_shinsei_scraping_service = SbiShinseiScrapingService()

# use_cases
rakuten_use_case = RakutenUseCase(
    session=session,
    scraping_service=rakuten_scraping_service,
    repository=rakuten_repository,
)
sbi_shinsei_use_case = SbiShinseiUseCase(
    session=session,
    scraping_service=sbi_shinsei_scraping_service,
    repository=sbi_shinsei_repository,
)

# routers
rakuten_bank_router = RakutenBankRouter(use_case=rakuten_use_case)
mitsuisumitomo_bank_router = MitsuisumitomoBankRouter()
sbi_shinsei_bank_router = SbiShinseiBankRouter(use_case=sbi_shinsei_use_case)
sumishin_sbi_bank_router = SumishinSbiBankRouter(prefix="/banks/sumishin_sbi")

# set routers
app.include_router(rakuten_bank_router.router)
app.include_router(mitsuisumitomo_bank_router.router)
app.include_router(sbi_shinsei_bank_router.router)
app.include_router(sumishin_sbi_bank_router.router)


# TODO: 2段階認証系はwebsocketでいけるか見てみる
@app.websocket("ws/banks/mitsuisumitomo")
async def save():
    pass
