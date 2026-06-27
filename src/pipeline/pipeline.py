class Pipeline:


    def __init__(

        self,

        detector,

        tracker,

        counter

    ):

        self.detector=detector

        self.tracker=tracker

        self.counter=counter



    def process(self,frame):


        detections = self.detector.detect(

            frame

        )


        tracks = self.tracker.update(

            detections

        )


        self.counter.update(

            tracks

        )


        return (

            tracks,

            self.counter.value()

        )