from db.db import session
from dotenv import load_dotenv
from fastapi import FastAPI
from repositories.rakuten_bank.repository import RepositoryImpl as RakutenRepository
from routers.mitsuisumitomo_bank import MitsuisumitomoBankRouter
from routers.rakuten_bank import RakutenBankRouter
from routers.sbi_shinsei_bank import SbiShinseiBankRouter
from routers.sumishin_sbi_bank import SumishinSbiBankRouter
from services.rakuten_bank.service import ServiceImpl as RakutenScrapingService
from use_cases.rakuten_bank.use_case import UseCase as RakutenUseCase

load_dotenv()

app = FastAPI()

# repositories
rakuten_repository = RakutenRepository()


# services
rakuten_scraping_service = RakutenScrapingService()


# use_cases
rakuten_use_case = RakutenUseCase(
    session=session,
    scraping_service=rakuten_scraping_service,
    repository=rakuten_repository,
)

# routers
rakuten_bank_router = RakutenBankRouter(use_case=rakuten_use_case)
mitsuisumitomo_bank_router = MitsuisumitomoBankRouter()
sbi_shinsei_bank_router = SbiShinseiBankRouter(prefix="/banks/sbi_shinsei")
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
