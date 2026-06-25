import cv2
import numpy as np



class ProductMatcher:


    def __init__(

        self,

        product_embedding,

        encoder,

        threshold=0.80

    ):


        self.product_embedding = product_embedding

        self.encoder = encoder

        self.threshold = threshold



    def cosine_similarity(

        self,

        a,

        b

    ):


        return np.dot(a,b) / (

            np.linalg.norm(a)

            *

            np.linalg.norm(b)

        )



    def filter(

        self,

        frame,

        detections

    ):


        matched=[]


        for detection in detections:


            x1,y1,x2,y2=detection["bbox"]



            crop=frame[

                y1:y2,

                x1:x2

            ]


            if crop.size==0:

                continue



            temp="temp_crop.jpg"



            cv2.imwrite(

                temp,

                crop

            )


            embedding=self.encoder.encode_image(

                temp

            )



            score=self.cosine_similarity(

                embedding,

                self.product_embedding

            )



            if score >= self.threshold:


                detection["similarity"]=float(score)


                matched.append(

                    detection

                )


        return matched