from ultralytics import YOLO


class Detector:


    def __init__(
        self,
        model_path,
        confidence=0.6
    ):

        self.model = YOLO(
            model_path
        )

        self.confidence = confidence



    def detect(self, frame):

        results = self.model(

            frame,

            imgsz=416,

            conf=self.confidence,

            device="cpu",

            verbose=False

        )


        detections=[]


        for result in results:


            boxes=result.boxes


            for box in boxes:


                x1,y1,x2,y2 = (

                    box.xyxy[0]
                    .cpu()
                    .numpy()

                )


                confidence=float(

                    box.conf[0]
                    .cpu()
                    .numpy()

                )



                detections.append({

                    "bbox":[

                        int(x1),
                        int(y1),
                        int(x2),
                        int(y2)

                    ],

                    "confidence":confidence

                })



        return detections