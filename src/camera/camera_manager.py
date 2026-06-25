import cv2


class CameraManager:

    def __init__(self, source=0):

        self.source = source

        self.cap = cv2.VideoCapture(
            source
        )


    def read(self):

        return self.cap.read()



    def release(self):

        if self.cap:

            self.cap.release()



    def is_opened(self):

        return self.cap.isOpened()