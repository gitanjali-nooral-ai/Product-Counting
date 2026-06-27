import cv2

from config.settings import settings

from src.camera.camera import Camera
from src.detection.detector import Detector
from src.tracking.tracker import Tracker
from src.counting.counter import Counter
from src.pipeline.pipeline import Pipeline
from src.visualization.draw import draw



# -------------------------
# Create pipeline
# -------------------------

pipeline = Pipeline(

    Detector(
        settings.model["path"]
    ),

    Tracker(),

    Counter()

)



# -------------------------
# Video input
# -------------------------

video_path = "data/videos/test_video.mp4"


camera = Camera(
    video_path
)



# Check video

if not camera.cap.isOpened():

    print(
        "ERROR: Cannot open video:",
        video_path
    )

    exit()



# -------------------------
# Processing loop
# -------------------------

while True:


    ret, frame = camera.read()


    if not ret:

        print(
            "Video finished"
        )

        break



    tracks, count = pipeline.process(

        frame

    )



    frame = draw(

        frame,

        tracks,

        count

    )



    cv2.imshow(

        "YOLO11n Counter",

        frame

    )



    key = cv2.waitKey(1)


    if key == 27:

        break



camera.release()

cv2.destroyAllWindows()


print(
    "FINAL COUNT:",
    count
)