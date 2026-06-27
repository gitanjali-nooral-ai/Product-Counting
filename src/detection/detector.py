from ultralytics import YOLO


class Detector:


    def __init__(self, path):

        self.model = YOLO(path)



    def detect(self, frame):

        results = self.model(

            frame,

            imgsz=416,

            conf=0.55,

            device="cpu",

            verbose=False

        )[0]


        detections=[]


        for box in results.boxes:


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


            class_id=int(

                box.cls[0]
                .cpu()
                .numpy()

            )


            detections.append({

                "bbox":[

                    x1,
                    y1,
                    x2,
                    y2

                ],

                "confidence":confidence,

                "class_id":class_id

            })


        return detections