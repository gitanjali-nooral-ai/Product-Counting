import numpy as np
import supervision as sv



def convert_to_sv(

    detections

):


    if len(detections)==0:


        return sv.Detections.empty()



    boxes=[]

    confidence=[]



    for d in detections:


        boxes.append(

            d["bbox"]

        )


        confidence.append(

            d["confidence"]

        )



    return sv.Detections(

        xyxy=np.array(

            boxes

        ),

        confidence=np.array(

            confidence

        )

    )