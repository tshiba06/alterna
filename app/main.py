from db.db import session
from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from repositories.mitsuisumitomo_bank.repository import (
    RepositoryImpl as MitsuisumitomoBankRepository,
)
from repositories.rakuten_bank.repository import RepositoryImpl as RakutenRepository
from repositories.sbi_benefit_system.repository import (
    RepositoryImpl as SbiBenefitSystemRepository,
)
from repositories.sbi_shinsei_bank.repository import (
    RepositoryImpl as SbiShinseiRepository,
)
from repositories.sumishin_sbi_bank.repository import (
    RepositoryImpl as SumishinSbiRepository,
)
from routers.mitsuisumitomo_bank import MitsuisumitomoBankRouter
from routers.mitsuisumitomo_bank_websocket import MitsuisumitomoBankWebsocketRouter
from routers.rakuten_bank import RakutenBankRouter
from routers.sbi_benefit_system import SbiBenefitSystemRouter
from routers.sbi_shinsei_bank import SbiShinseiBankRouter
from routers.sumishin_sbi_bank import SumishinSbiBankRouter
from app.routers.mitsuisumitomo_card import router as mitsuisumitomo_card_router # Added import
from services.mitsuisumitomo_bank.service import (
    ServiceImpl as MitsuisumitomoBankService,
)
from services.rakuten_bank.service import ServiceImpl as RakutenScrapingService
from services.sbi_benefit_system.service import ServiceImpl as SbiBenefitSystemService
from services.sbi_shinsei_bank.service import ServiceImpl as SbiShinseiScrapingService
from services.sumishin_sbi_bank.service import ServiceImpl as SumishinSbiScrapingService
from use_cases.mitsuisumitomo_bank.use_case import UseCase as MitsuisumitomoBankUseCase
from use_cases.rakuten_bank.use_case import UseCase as RakutenUseCase
from use_cases.sbi_benefit_system.use_case import UseCase as SbiBenefitSystemUseCase
from use_cases.sbi_shinsei_bank.use_case import UseCase as SbiShinseiUseCase
from use_cases.sumishin_sbi_bank.use_case import UseCase as SumishinSbiUseCase

load_dotenv()

app = FastAPI()

# middleware
origins = ["http://localhost:9000"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# repositories
rakuten_repository = RakutenRepository()
sbi_shinsei_repository = SbiShinseiRepository()
sumishin_sbi_repository = SumishinSbiRepository()
sbi_benefit_system_repository = SbiBenefitSystemRepository()
mitsuisumitomo_bank_repository = MitsuisumitomoBankRepository()

# services
rakuten_scraping_service = RakutenScrapingService()
sbi_shinsei_scraping_service = SbiShinseiScrapingService()
sumishin_sbi_scraping_service = SumishinSbiScrapingService()
sbi_benefit_system_scraping_service = SbiBenefitSystemService()
mitsuisumitomo_bank_scraping_service = MitsuisumitomoBankService()

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
sumishin_sbi_use_case = SumishinSbiUseCase(
    session=session,
    scraping_service=sumishin_sbi_scraping_service,
    repository=sumishin_sbi_repository,
)
sbi_benefit_system_use_case = SbiBenefitSystemUseCase(
    session=session,
    scraping_service=sbi_benefit_system_scraping_service,
    repository=sbi_benefit_system_repository,
)
mitsuisumitomo_bank_use_case = MitsuisumitomoBankUseCase(
    session=session,
    scraping_service=mitsuisumitomo_bank_scraping_service,
    repository=mitsuisumitomo_bank_repository,
)

# routers
rakuten_bank_router = RakutenBankRouter(use_case=rakuten_use_case)
mitsuisumitomo_bank_router = MitsuisumitomoBankRouter()
sbi_shinsei_bank_router = SbiShinseiBankRouter(use_case=sbi_shinsei_use_case)
sumishin_sbi_bank_router = SumishinSbiBankRouter(use_case=sumishin_sbi_use_case)
sbi_benefit_system_router = SbiBenefitSystemRouter(use_case=sbi_benefit_system_use_case)
mitsuisumitomo_bank_websocket_router = MitsuisumitomoBankWebsocketRouter(
    use_case=mitsuisumitomo_bank_use_case
)


# set routers
app.include_router(rakuten_bank_router.router)
app.include_router(mitsuisumitomo_bank_router.router)
app.include_router(sbi_shinsei_bank_router.router)
app.include_router(sumishin_sbi_bank_router.router)
app.include_router(sbi_benefit_system_router.router)
app.include_router(mitsuisumitomo_bank_websocket_router.router)
app.include_router(mitsuisumitomo_card_router) # Added router


# TODO: 2段階認証系はwebsocketでいけるか見てみる
@app.websocket("ws/banks/mitsuisumitomo")
async def save():
    pass
