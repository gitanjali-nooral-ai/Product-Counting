from datetime import datetime, timedelta



class StatisticsService:


    def __init__(
        self,
        database,
        state=None
    ):

        self.database = database
        self.state = state



    # -----------------------------
    # Current live count
    # -----------------------------

    def current_count(self):

        if self.state:

            return self.state.get_count()

        return 0



    # -----------------------------
    # Total count
    # -----------------------------

    def total_count(
        self,
        product_id=None
    ):


        query = """
        SELECT COUNT(*)
        FROM count_events
        """

        params = []



        if product_id is not None:

            query += """
            WHERE product_id=?
            """

            params.append(product_id)



        row = self.database.conn.execute(
            query,
            params
        ).fetchone()



        return row[0] if row else 0




    # -----------------------------
    # Today count
    # -----------------------------

    def today_count(
        self,
        product_id=None
    ):


        today = datetime.now().date().isoformat()



        query = """
        SELECT COUNT(*)
        FROM count_events
        WHERE DATE(counted_at)=?
        """



        params=[today]



        if product_id is not None:

            query += """
            AND product_id=?
            """

            params.append(product_id)



        row = self.database.conn.execute(
            query,
            params
        ).fetchone()



        return row[0] if row else 0





    # -----------------------------
    # Hourly count
    # -----------------------------

    def hourly_count(
        self,
        product_id=None
    ):


        query = """
        SELECT
            strftime('%H', counted_at),
            COUNT(*)

        FROM count_events
        """



        params=[]



        if product_id is not None:

            query += """
            WHERE product_id=?
            """

            params.append(product_id)



        query += """
        GROUP BY strftime('%H', counted_at)
        ORDER BY 1
        """



        rows = self.database.conn.execute(
            query,
            params
        ).fetchall()



        return [

            {
                "hour": row[0],
                "count": row[1]
            }

            for row in rows

        ]





    # -----------------------------
    # Daily count
    # -----------------------------

    def daily_count(
        self,
        product_id=None,
        days=30
    ):


        start_date = (

            datetime.now()
            -
            timedelta(days=days)

        ).date().isoformat()



        query = """
        SELECT
            DATE(counted_at),
            COUNT(*)

        FROM count_events

        WHERE DATE(counted_at)>=?

        """



        params=[start_date]



        if product_id is not None:

            query += """
            AND product_id=?
            """

            params.append(product_id)



        query += """
        GROUP BY DATE(counted_at)

        ORDER BY DATE(counted_at)
        """



        rows = self.database.conn.execute(
            query,
            params
        ).fetchall()



        return [

            {
                "date": row[0],
                "count": row[1]
            }

            for row in rows

        ]





    # -----------------------------
    # Weekly count
    # -----------------------------

    def weekly_count(
        self,
        product_id=None
    ):


        query="""

        SELECT

            strftime('%Y-%W', counted_at),

            COUNT(*)


        FROM count_events

        """



        params=[]



        if product_id is not None:

            query += """
            WHERE product_id=?
            """

            params.append(product_id)



        query += """

        GROUP BY strftime('%Y-%W', counted_at)

        ORDER BY 1

        """



        rows=self.database.conn.execute(
            query,
            params
        ).fetchall()



        return [

            {
                "week":row[0],
                "count":row[1]
            }

            for row in rows

        ]





    # -----------------------------
    # Monthly count
    # -----------------------------

    def monthly_count(
        self,
        product_id=None
    ):


        query="""

        SELECT

            strftime('%Y-%m', counted_at),

            COUNT(*)


        FROM count_events

        """



        params=[]



        if product_id is not None:

            query += """
            WHERE product_id=?
            """

            params.append(product_id)



        query += """

        GROUP BY strftime('%Y-%m', counted_at)

        ORDER BY 1

        """



        rows=self.database.conn.execute(
            query,
            params
        ).fetchall()



        return [

            {
                "month":row[0],
                "count":row[1]
            }

            for row in rows

        ]