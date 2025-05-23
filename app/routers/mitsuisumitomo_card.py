from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session

from app.db.db import get_session
from app.internal.log import logger # Assuming you have a logger setup
from app.repositories.mitsuisumitomo_card.repository import (
    RepositoryImpl as SMCCardRepositoryImpl,
)
from app.services.mitsuisumitomo_card.service import (
    ServiceImpl as SMCCardScrapingServiceImpl,
)
from app.use_cases.mitsuisumitomo_card.model import GetHistoriesOutput
from app.use_cases.mitsuisumitomo_card.use_case import UseCase as SMCCardUseCase

# If app.routers.router.Router is a base class you use, import it
# from app.routers.router import Router 
# Otherwise, just use APIRouter directly.

# router = APIRouter(prefix="/cards/mitsuisumitomo", tags=["Mitsui Sumitomo Card"])
# Assuming you might have a base Router class like in other files, let's use a simple APIRouter for now.
# If your project has a convention for a base class (e.g. app.routers.router.Router), adapt to that.
# For now, we will define it directly.

router = APIRouter(
    prefix="/cards/mitsuisumitomo", # Changed prefix to /cards
    tags=["Mitsui Sumitomo Card"],
)

def get_smc_card_use_case(
    db: Session = Depends(get_session),
) -> SMCCardUseCase:
    repository = SMCCardRepositoryImpl()
    scraping_service = SMCCardScrapingServiceImpl()
    return SMCCardUseCase(
        db_session=db,
        smc_card_repository=repository,
        smc_card_scraping_service=scraping_service,
    )

@router.post("/save", status_code=status.HTTP_200_OK)
async def save_smc_card_data(
    use_case: SMCCardUseCase = Depends(get_smc_card_use_case),
):
    logger.info("Saving Mitsui Sumitomo Card data")
    try:
        result_status = await use_case.create_history()
        if result_status == 200:
            return JSONResponse(
                content={"message": "Mitsui Sumitomo Card data saved successfully"},
                status_code=status.HTTP_200_OK,
            )
        else:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="Failed to save Mitsui Sumitomo Card data",
            )
    except Exception as e:
        logger.error(f"Error saving Mitsui Sumitomo Card data: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="An unexpected error occurred",
        )

@router.get("/latest", status_code=status.HTTP_200_OK)
def get_latest_smc_card_total(
    use_case: SMCCardUseCase = Depends(get_smc_card_use_case),
):
    total = use_case.get_latest_total()
    if total is None:
        return JSONResponse(content={"total": None, "message": "No data found"}, status_code=status.HTTP_200_OK)
    return JSONResponse(content={"total": total}, status_code=status.HTTP_200_OK)

@router.get("/history", response_model=GetHistoriesOutput)
def get_smc_card_history(
    use_case: SMCCardUseCase = Depends(get_smc_card_use_case),
):
    history = use_case.get_histories()
    return history
