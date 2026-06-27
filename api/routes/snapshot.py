from fastapi import APIRouter, HTTPException

import cv2
import os
import uuid

from datetime import datetime


from services.pipeline_state import state
from config.settings import settings



router = APIRouter(

    prefix="/camera",

    tags=["Camera"]

)





@router.post("/snapshot")
def save_snapshot():



    if not state.running:

        raise HTTPException(

            status_code=400,

            detail="Camera is not running"

        )



    if state.latest_frame is None:

        raise HTTPException(

            status_code=400,

            detail="No frame available"

        )




    folder = settings.storage["snapshots"]



    os.makedirs(

        folder,

        exist_ok=True

    )




    filename = (

        datetime.now()

        .strftime("%Y%m%d_%H%M%S")

        +

        "_"

        +

        str(uuid.uuid4())[:8]

        +

        ".jpg"

    )



    path = os.path.join(

        folder,

        filename

    )




    frame = state.latest_frame.copy()



    success = cv2.imwrite(

        path,

        frame

    )



    if not success:

        raise HTTPException(

            status_code=500,

            detail="Failed to save snapshot"

        )




    return {


        "saved": True,


        "file": path,


        "timestamp":

            datetime.now().isoformat(),



        "product": {


            "id":

                state.product_id,


            "name":

                state.product_name

        },



        "count":

            state.count,



        "fps":

            state.fps

    }