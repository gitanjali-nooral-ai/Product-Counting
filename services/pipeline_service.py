import threading


from workers.camera_worker import CameraWorker



class PipelineService:


    def __init__(self):


        self.worker=None

        self.thread=None

        self.running=False



    def start(

        self,

        product_id

    ):


        if self.running:

            return False



        self.running=True



        self.worker=CameraWorker(

            product_id,

            self

        )



        self.thread=threading.Thread(

            target=self.worker.run

        )



        self.thread.daemon=True


        self.thread.start()



        return True



    def stop(self):


        self.running=False



    def status(self):


        return self.running