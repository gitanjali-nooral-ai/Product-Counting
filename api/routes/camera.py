from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from services.pipeline_service import PipelineService
from services.pipeline_state import state
from src.database.database import Database
from config.settings import settings


router = APIRouter(
    prefix="/camera",
    tags=["Camera"]
)


pipeline_service = PipelineService()

database = Database(
    settings.database["path"]
)


class CameraCreate(BaseModel):

    name: str
    type: str
    source: str
    width: int = 640
    height: int = 480



@router.post("/")
def add_camera(camera: CameraCreate):

    camera_id = database.add_camera(
        camera.name,
        camera.type,
        camera.source,
        camera.width,
        camera.height
    )

    return {

        "id": camera_id,

        "message": "Camera added"

    }



@router.get("/")
def get_cameras():

    return database.get_cameras()



@router.get("/{camera_id}")
def get_camera(camera_id:int):

    camera = database.get_camera(
        camera_id
    )

    if not camera:

        raise HTTPException(
            status_code=404,
            detail="Camera not found"
        )


    return camera




@router.delete("/{camera_id}")
def delete_camera(camera_id:int):

    deleted = database.delete_camera(
        camera_id
    )


    return {

        "deleted": deleted

    }





@router.post("/start/{camera_id}/{product_id}")
def start_camera(
    camera_id:int,
    product_id:int
):


    try:

        started = pipeline_service.start(

            product_id,

            camera_id

        )


        return {

            "camera_started": started,

            "camera_id": camera_id,

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


        "camera":

        {

            "id":

                getattr(
                    state,
                    "camera_id",
                    None
                )

        },


        "count":

            state.count,


        "fps":

            state.fps,


        "last_update":

            state.last_update

    }