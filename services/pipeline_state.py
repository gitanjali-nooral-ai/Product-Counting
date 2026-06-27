import time
import threading



class PipelineState:


    def __init__(self):


        self.running = False


        self.product_id = None

        self.product_name = None


        self.count = 0

        self.fps = 0


        self.latest_frame = None


        self.last_update = None


        self.lock = threading.Lock()



    # -------------------------
    # Camera control
    # -------------------------

    def start(self):

        with self.lock:

            self.running = True



    def stop(self):

        with self.lock:

            self.running = False



    def is_running(self):

        with self.lock:

            return self.running



    # -------------------------
    # Reset
    # -------------------------

    def reset(self):

        with self.lock:

            self.count = 0

            self.fps = 0

            self.latest_frame = None

            self.last_update = None

            self.product_id = None

            self.product_name = None



    # -------------------------
    # Product
    # -------------------------

    def update_product(
        self,
        product_id,
        name=None
    ):

        with self.lock:

            self.product_id = product_id

            self.product_name = name



    # -------------------------
    # Frame
    # -------------------------

    def update_frame(
        self,
        frame
    ):


        if frame is None:

            return


        with self.lock:

            self.latest_frame = frame.copy()

            self.last_update = time.time()



    def get_frame(self):

        with self.lock:

            if self.latest_frame is None:

                return None


            return self.latest_frame.copy()



    # -------------------------
    # Count
    # -------------------------

    def update_count(
        self,
        count
    ):

        with self.lock:

            self.count = max(
                0,
                int(count)
            )



    def get_count(self):

        with self.lock:

            return self.count



    # -------------------------
    # FPS
    # -------------------------

    def update_fps(
        self,
        fps
    ):

        with self.lock:

            self.fps = max(
                0,
                float(fps)
            )



    # -------------------------
    # Status
    # -------------------------

    def get_status(self):

        with self.lock:

            return {


                "running":

                    self.running,


                "product":

                {

                    "id":

                        self.product_id,


                    "name":

                        self.product_name

                },


                "count":

                    self.count,


                "fps":

                    round(
                        self.fps,
                        2
                    ),


                "last_update":

                    self.last_update

            }




state = PipelineState()