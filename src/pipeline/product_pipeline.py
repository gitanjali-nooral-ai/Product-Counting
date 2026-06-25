from src.utils.converter import convert_to_sv



class ProductPipeline:


    def __init__(

        self,

        detector,

        matcher,

        tracker,

        counter,

        database,

        product_id

    ):


        self.detector=detector

        self.matcher=matcher

        self.tracker=tracker

        self.counter=counter

        self.database=database

        self.product_id=product_id



    def process(

        self,

        frame

    ):


        detections=self.detector.detect(

            frame

        )


        detections=self.matcher.filter(

            frame,

            detections

        )



        sv_detections=convert_to_sv(

            detections

        )


        tracked=self.tracker.update(

            sv_detections

        )



        counted=self.counter.update(

            tracked

        )



        for track_id in counted:


            self.database.add_count(

                self.product_id,

                track_id

            )



        return tracked,self.counter.get_count()