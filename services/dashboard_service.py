class DashboardService:


    def __init__(
        self,
        state,
        statistics
    ):

        self.state = state

        self.statistics = statistics




    def get_dashboard(self):


        status = self.state.get_status()



        return {


            "camera_running":

                status["running"],



            "current_count":

                status["count"],



            "fps":

                status["fps"],



            "product":

            {

                "id":

                    status["product"]["id"],



                "name":

                    status["product"]["name"]

            },



            "statistics":

            {

                "today":

                    self.statistics.today_count(),



                "total":

                    self.statistics.total_count()

            },



            "last_update":

                status["last_update"]

        }