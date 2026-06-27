from fastapi import APIRouter, Query

from src.database.database import Database
from services.statistics_service import StatisticsService
from services.pipeline_state import state
from config.settings import settings


router = APIRouter(
    prefix="/statistics",
    tags=["Statistics"]
)


database = Database(
    settings.database["path"]
)


service = StatisticsService(
    database,
    state
)


# ---------------------------------
# Live count
# ---------------------------------

@router.get("/current")
def current():

    return {

        "live_count": state.count,

        "product": {

            "id": state.product_id,

            "name": state.product_name

        },

        "fps": state.fps

    }



# ---------------------------------
# Today count
# ---------------------------------

@router.get("/today")
def today(
    product_id: int | None = None
):

    return {

        "date": "today",

        "count":
            service.today_count(
                product_id=product_id
            )

    }



# ---------------------------------
# Hourly report
# ---------------------------------

@router.get("/hourly")
def hourly(
    product_id: int | None = None
):

    return {

        "chart": "hourly",

        "data":
            service.hourly_count(
                product_id=product_id
            )

    }



# ---------------------------------
# Daily report
# ---------------------------------

@router.get("/daily")
def daily(
    days: int = Query(
        30,
        ge=1,
        le=365
    ),

    product_id: int | None = None
):

    return {

        "chart": "daily",

        "days": days,

        "data":
            service.daily_count(

                days=days,

                product_id=product_id

            )

    }



# ---------------------------------
# Weekly report
# ---------------------------------

@router.get("/weekly")
def weekly(
    product_id: int | None = None
):

    return {

        "chart": "weekly",

        "data":
            service.weekly_count(

                product_id=product_id

            )

    }



# ---------------------------------
# Monthly report
# ---------------------------------

@router.get("/monthly")
def monthly(
    product_id: int | None = None
):

    return {

        "chart": "monthly",

        "data":
            service.monthly_count(

                product_id=product_id

            )

    }