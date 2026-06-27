from fastapi import APIRouter

from services.pipeline_state import state
from services.statistics_service import StatisticsService
from services.dashboard_service import DashboardService

from src.database.database import Database
from config.settings import settings



router = APIRouter(

    prefix="/dashboard",

    tags=["Dashboard"]

)



database = Database(

    settings.database["path"]

)



statistics = StatisticsService(

    database,

    state

)



service = DashboardService(

    state,

    statistics

)




@router.get("/")
def dashboard():


    return service.get_dashboard()