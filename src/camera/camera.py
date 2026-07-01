import cv2



class Camera:


    def __init__(self, source):


        if isinstance(source, str):

            if source.isdigit():

                source = int(source)



        self.cap = cv2.VideoCapture(
            source
        )



    def read(self):

        return self.cap.read()



    def release(self):

        if self.cap:

            self.cap.release()