import time
import traceback


from src.camera.camera import Camera
from src.detection.detector import Detector
from src.tracking.tracker import Tracker
from src.counting.counter import Counter
from src.pipeline.pipeline import Pipeline
from src.database.database import Database


from config.settings import settings
from services.pipeline_state import state




class CameraWorker:


    def __init__(
        self,
        product_id=None
    ):

        self.product_id = product_id




    def run(self):


        print(
            "Camera worker started"
        )



        camera = None



        try:


            database = Database(

                settings.database["path"]

            )



            pipeline = Pipeline(


                Detector(

                    settings.model["path"]

                ),


                Tracker(),


                Counter()

            )



            camera = Camera(

                settings.camera["source"]

            )



            state.update_product(

                self.product_id

            )



            while state.is_running():



                ret, frame = camera.read()



                if not ret:


                    print(
                        "Frame failed"
                    )

                    break



                start = time.time()



                tracks, count = pipeline.process(

                    frame

                )



                state.update_count(

                    count

                )



                state.update_frame(

                    frame

                )



                elapsed = time.time() - start



                if elapsed > 0:


                    state.update_fps(

                        round(
                            1 / elapsed,
                            2
                        )

                    )



                #
                # Save detected events
                #
                for track in tracks:


                    if track.get("counted"):


                        database.add_count_event(

                            self.product_id,

                            track["id"]

                        )




        except Exception as e:


            print(
                "Worker error:",
                e
            )


            traceback.print_exc()



        finally:



            if camera:

                camera.release()



            state.stop()



            print(

                "Camera worker stopped"

            )