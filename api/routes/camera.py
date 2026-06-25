from fastapi import APIRouter


from services.pipeline_service import PipelineService



router = APIRouter(

    prefix="/camera",

    tags=["Camera"]

)



pipeline_service = PipelineService()



@router.post("/start/{product_id}")
def start_camera(

    product_id:int

):


    result = pipeline_service.start(

        product_id

    )



    return {


        "camera_started":

        result,


        "product_id":

        product_id

    }




@router.post("/stop")
def stop_camera():


    pipeline_service.stop()



    return {


        "status":

        "camera stopped"

    }




@router.get("/status")
def camera_status():


    return {


        "running":

        pipeline_service.status()

    }