import supervision as sv
import numpy as np



class Tracker:


    def __init__(self):

        self.byte = sv.ByteTrack()



    def update(self, detections):


        if len(detections)==0:

            return sv.Detections.empty()



        boxes=[]

        confidence=[]

        classes=[]



        for d in detections:


            boxes.append(
                d["bbox"]
            )


            confidence.append(

                d["confidence"]

            )


            classes.append(

                d["class_id"]

            )



        sv_detections = sv.Detections(

            xyxy=np.array(

                boxes,

                dtype=np.float32

            ),


            confidence=np.array(

                confidence,

                dtype=np.float32

            ),


            class_id=np.array(

                classes

            )

        )



        return self.byte.update_with_detections(

            sv_detections

        )