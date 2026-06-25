from fastapi import APIRouter

import pandas as pd


from src.database.sqlite_manager import Database



router = APIRouter(

    prefix="/reports",

    tags=["Reports"]

)



database = Database(

    "data/database/production.db"

)



@router.get("/counts")
def get_counts():


    cursor = database.conn.cursor()



    result = cursor.execute(

    """

    SELECT

    products.product_name,

    count_events.track_id,

    count_events.counted_at


    FROM count_events


    JOIN products


    ON products.id=count_events.product_id


    ORDER BY counted_at DESC


    """

    ).fetchall()



    return {


        "events":

        result

    }



@router.get("/csv")
def export_csv():


    cursor=database.conn.cursor()



    data=cursor.execute(

    """

    SELECT

    products.product_name,

    count_events.track_id,

    count_events.counted_at


    FROM count_events


    JOIN products


    ON products.id=count_events.product_id

    """

    ).fetchall()



    df=pd.DataFrame(

        data,

        columns=[

            "product",

            "tracking_id",

            "time"

        ]

    )


    path="data/reports/count_report.csv"



    df.to_csv(

        path,

        index=False

    )



    return {


        "file":

        path

    }