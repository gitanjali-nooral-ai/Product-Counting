class Counter:


    def __init__(self):

        self.ids=set()



    def update(self,tracks):


        if tracks.tracker_id is None:

            return



        for i in tracks.tracker_id:

            self.ids.add(
                int(i)
            )



    def value(self):

        return len(self.ids)