from fastapi import APIRouter, HTTPException

from services.pipeline_service import PipelineService
from services.pipeline_state import state



router = APIRouter(
    prefix="/camera",
    tags=["Camera"]
)



pipeline_service = PipelineService()



@router.post("/start/{product_id}")
def start_camera(product_id:int):


    try:

        started = pipeline_service.start(
            product_id
        )


        return {

            "camera_started": started,

            "product_id": product_id,

            "message":

                "Camera started"

                if started

                else

                "Camera already running"

        }


    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=str(e)
        )




@router.post("/stop")
def stop_camera():


    stopped = pipeline_service.stop()


    return {

        "camera_stopped": stopped,

        "message": "Camera stopped"

    }




@router.get("/status")
def camera_status():


    return pipeline_service.status()




@router.get("/info")
def camera_info():


    return {

        "running":

            state.running,


        "product":

        {

            "id":

                state.product_id,


            "name":

                state.product_name

        },


        "count":

            state.count,


        "fps":

            state.fps,


        "last_update":

            state.last_update

    }