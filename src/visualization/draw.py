import cv2



def draw(frame,tracks,count):


    if tracks.tracker_id is None:

        return frame



    for i,id in enumerate(
        tracks.tracker_id
    ):


        x1,y1,x2,y2=map(
            int,
            tracks.xyxy[i]
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

            f"ID {id}",

            (x1,y1-10),

            cv2.FONT_HERSHEY_SIMPLEX,

            .6,

            (0,255,0),

            2

        )



    cv2.putText(

        frame,

        f"COUNT {count}",

        (30,50),

        cv2.FONT_HERSHEY_SIMPLEX,

        1,

        (0,0,255),

        3

    )


    return frame