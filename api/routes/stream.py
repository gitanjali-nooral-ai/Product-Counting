from fastapi import APIRouter
from fastapi.responses import StreamingResponse

import cv2
import time
import traceback


from services.pipeline_state import state



router = APIRouter(
    prefix="/camera",
    tags=["Camera"]
)




def generate_frames():


    while True:


        try:


            # Camera stopped

            if not state.running:


                time.sleep(0.2)

                continue




            # Frame unavailable

            if state.latest_frame is None:


                time.sleep(0.05)

                continue




            # Safe copy

            frame = state.latest_frame.copy()



            # -------------------------
            # Overlay count
            # -------------------------

            cv2.putText(

                frame,

                f"Count: {state.count}",

                (30,50),

                cv2.FONT_HERSHEY_SIMPLEX,

                1.5,

                (0,0,255),

                3

            )



            # -------------------------
            # Overlay FPS
            # -------------------------

            cv2.putText(

                frame,

                f"FPS: {state.fps:.2f}",

                (30,90),

                cv2.FONT_HERSHEY_SIMPLEX,

                1,

                (0,255,0),

                2

            )




            # -------------------------
            # Encode JPEG
            # -------------------------

            success, buffer = cv2.imencode(

                ".jpg",

                frame,

                [

                    cv2.IMWRITE_JPEG_QUALITY,

                    85

                ]

            )



            if not success:

                continue




            jpg = buffer.tobytes()




            yield (

                b"--frame\r\n"

                b"Content-Type: image/jpeg\r\n\r\n"

                +

                jpg

                +

                b"\r\n"

            )



            time.sleep(0.03)



        except GeneratorExit:


            # Browser closed stream

            break



        except Exception as e:


            print(
                "Stream error:",
                e
            )

            traceback.print_exc()


            time.sleep(1)





@router.get("/stream")
def stream():


    return StreamingResponse(

        generate_frames(),

        media_type=

        "multipart/x-mixed-replace; boundary=frame"

    )