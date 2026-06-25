import supervision as sv



class ProductTracker:


    def __init__(self):


        self.tracker = sv.ByteTrack()



    def update(

        self,

        detections

    ):


        return self.tracker.update_with_detections(

            detections

        )