from fastapi import APIRouter
import os

from src.database.database import Database
from config.settings import settings
from services.pipeline_state import state



router = APIRouter(
    prefix="/health",
    tags=["Health"]
)



# Shared database connection

database = Database(
    settings.database["path"]
)




@router.get("/")
def health():


    database_status = False


    try:

        database.conn.execute(
            "SELECT 1"
        )

        database_status = True


    except Exception:

        database_status = False




    model_path = settings.model["path"]


    model_status = os.path.isfile(
        model_path
    )



    return {


        "status": "running",



        "database": database_status,



        "model": {

            "path": model_path,

            "loaded": model_status

        },



        "camera": {

            "running":

                state.running,


            "fps":

                state.fps,


            "count":

                state.count

        },



        "product": {

            "id":

                state.product_id,


            "name":

                state.product_name

        }

    }