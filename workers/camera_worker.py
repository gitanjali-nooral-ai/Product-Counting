from src.camera.camera_manager import CameraManager


from src.detection.detector import Detector


from src.embedding.clip_encoder import CLIPEncoder


from src.matching.matcher import ProductMatcher


from src.tracking.tracker import ProductTracker


from src.counting.counter import ProductCounter


from src.pipeline.product_pipeline import ProductPipeline


from src.database.sqlite_manager import Database



class CameraWorker:


    def __init__(

        self,

        product_id,

        service

    ):


        self.product_id=product_id

        self.service=service



    def run(self):


        print(
            "Camera worker started"
        )



        database=Database(

            "data/database/production.db"

        )



        # Load selected product


        product=database.conn.execute(

        """

        SELECT *

        FROM products

        WHERE id=?

        """,

        (

        self.product_id,

        )

        ).fetchone()



        if product is None:


            print(
                "Product not found"
            )

            return



        encoder=CLIPEncoder()



        embedding=encoder.load_embedding(

            product[3]

        )



        matcher=ProductMatcher(

            embedding,

            encoder

        )



        pipeline=ProductPipeline(

            detector=Detector(

                "data/models/yolov8n.pt"

            ),

            matcher=matcher,

            tracker=ProductTracker(),

            counter=ProductCounter(

                400

            ),

            database=database,

            product_id=self.product_id

        )



        camera=CameraManager(

            0

        )



        while self.service.running:



            ret,frame=camera.read()



            if not ret:

                break



            tracked,count=pipeline.process(

                frame

            )



            print(

                "Current Count:",

                count

            )



        camera.release()



        print(

            "Camera worker stopped"

        )