class ProductCounter:


    def __init__(

        self,

        line_position

    ):


        self.line_position=line_position


        self.counted_ids=set()


        self.total=0



    def update(

        self,

        tracked

    ):


        new_counts=[]


        if tracked.tracker_id is None:

            return new_counts



        for index,track_id in enumerate(

            tracked.tracker_id

        ):


            x1,y1,x2,y2=tracked.xyxy[index]


            center_y=(y1+y2)/2



            if center_y > self.line_position:


                track_id=int(track_id)



                if track_id not in self.counted_ids:


                    self.counted_ids.add(

                        track_id

                    )


                    self.total+=1


                    new_counts.append(

                        track_id

                    )


        return new_counts



    def get_count(self):

        return self.total