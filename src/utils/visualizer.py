import cv2



class Visualizer:



    def draw(

        self,

        frame,

        tracked,

        product_name

    ):


        if tracked.tracker_id is None:

            return frame



        for i,track_id in enumerate(

            tracked.tracker_id

        ):


            x1,y1,x2,y2=map(

                int,

                tracked.xyxy[i]

            )



            cv2.rectangle(

                frame,

                (x1,y1),

                (x2,y2),

                (0,255,0),

                2

            )



            cv2.putText(

                frame,

                f"{product_name} ID:{track_id}",

                (x1,y1-10),

                cv2.FONT_HERSHEY_SIMPLEX,

                0.6,

                (0,255,0),

                2

            )


        return frame