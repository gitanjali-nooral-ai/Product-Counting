import threading
import traceback

from workers.camera_worker import CameraWorker
from services.pipeline_state import state



class PipelineService:


    def __init__(self):

        self.worker = None

        self.thread = None

        self.error = None



    # ---------------------------------
    # Worker wrapper
    # ---------------------------------

    def _run_worker(self):

        try:

            self.worker.run()


        except Exception as e:

            self.error = str(e)

            traceback.print_exc()


        finally:

            state.running = False





    # ---------------------------------
    # Start pipeline
    # ---------------------------------

    def start(
        self,
        product_id=None
    ):


        if state.running:

            return False



        # Reset runtime state

        state.count = 0

        state.fps = 0

        state.latest_frame = None

        state.product_id = product_id



        # Reset error

        self.error = None



        state.running = True



        try:


            self.worker = CameraWorker(

                product_id

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





    # ---------------------------------
    # Stop pipeline
    # ---------------------------------

    def stop(self):


        if not state.running:

            return False



        state.running = False



        if self.worker:


            # if worker supports stop

            if hasattr(
                self.worker,
                "stop"
            ):

                try:

                    self.worker.stop()

                except Exception:

                    traceback.print_exc()



        if self.thread:


            self.thread.join(

                timeout=5

            )



        self.thread = None

        self.worker = None



        state.latest_frame = None

        state.fps = 0



        return True





    # ---------------------------------
    # Status
    # ---------------------------------

    def status(self):


        product_name = None


        if hasattr(
            state,
            "product_name"
        ):

            product_name = state.product_name



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

                    getattr(
                        state,
                        "product_id",
                        None
                    ),



                "name":

                    product_name

            },


            "error":

                self.error

        }