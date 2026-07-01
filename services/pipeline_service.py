import threading
import traceback

from workers.camera_worker import CameraWorker
from services.pipeline_state import state



class PipelineService:


    def __init__(self):

        self.worker = None
        self.thread = None
        self.error = None




    def _run_worker(self):

        try:

            self.worker.run()


        except Exception as e:

            self.error = str(e)

            traceback.print_exc()


        finally:

            state.running = False





    def start(
        self,
        product_id=None,
        camera_id=None,
        camera_source=None
    ):


        if state.running:

            return False



        state.count = 0

        state.fps = 0

        state.latest_frame = None

        state.product_id = product_id

        state.camera_id = camera_id



        self.error = None


        state.running = True



        try:


            self.worker = CameraWorker(

                product_id,

                camera_source

            )


            self.thread = threading.Thread(

                target=self._run_worker,

                daemon=True

            )


            self.thread.start()



            return True



        except Exception as e:


            state.running = False

            self.error = str(e)

            traceback.print_exc()


            return False





    def stop(self):

        if not state.running:

            return False


        state.running = False


        if self.thread:

            self.thread.join(
                timeout=5
            )


        self.thread = None

        self.worker = None


        state.latest_frame = None

        state.fps = 0


        return True





    def status(self):


        return {

            "running":

                bool(
                    state.running
                ),

            "count":

                state.count,


            "fps":

                round(
                    state.fps,
                    2
                ),


            "product":

            {

                "id":

                    state.product_id

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


            "error":

                self.error

        }