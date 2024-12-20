from fastapi import FastAPI
from routers.mitsuisumitomo_bank import MitsuisumitomoBankRouter
from routers.rakuten_bank import RakutenBankRouter
from routers.sbi_shinsei_bank import SbiShinseiBankRouter
from routers.sumishin_sbi_bank import SumishinSbiBankRouter

app = FastAPI()

# routers
rakuten_bank_router = RakutenBankRouter(prefix="/banks/rakuten")
mitsuisumitomo_bank_router = MitsuisumitomoBankRouter(prefix="/banks/mitsuisumitomo")
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
