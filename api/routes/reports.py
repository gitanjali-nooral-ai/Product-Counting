from fastapi import APIRouter, Query

import os
import pandas as pd


from src.database.database import Database
from config.settings import settings



router = APIRouter(
    prefix="/reports",
    tags=["Reports"]
)



database = Database(
    settings.database["path"]
)





# ------------------------------------
# Count events report
# ------------------------------------

@router.get("/counts")
def get_counts(

    product_id: int | None = None,

    limit: int = Query(
        100,
        ge=1,
        le=1000
    )

):


    query = """

    SELECT

        count_events.id,

        products.id,

        products.name,

        count_events.counted_at


    FROM count_events


    LEFT JOIN products

    ON products.id = count_events.product_id

    """


    params = []



    if product_id is not None:

        query += """

        WHERE products.id=?

        """

        params.append(product_id)



    query += """

    ORDER BY count_events.id DESC

    LIMIT ?

    """


    params.append(limit)



    rows = database.conn.execute(

        query,

        params

    ).fetchall()



    events = []



    for row in rows:

        events.append({

            "event_id": row[0],

            "product_id": row[1],

            "product_name": row[2] or "Unknown",

            "counted_at": row[3]

        })



    return {

        "total": len(events),

        "events": events

    }





# ------------------------------------
# CSV Export
# ------------------------------------

@router.get("/csv")
def export_csv(

    product_id: int | None = None

):


    query = """

    SELECT


        products.name,


        count_events.counted_at



    FROM count_events



    LEFT JOIN products



    ON products.id = count_events.product_id



    """



    params = []



    if product_id is not None:


        query += """

        WHERE products.id=?

        """


        params.append(product_id)




    rows = database.conn.execute(

        query,

        params

    ).fetchall()




    df = pd.DataFrame(

        rows,

        columns=[

            "product",

            "time"

        ]

    )




    report_folder = settings.storage["reports"]



    os.makedirs(

        report_folder,

        exist_ok=True

    )




    path = os.path.join(

        report_folder,

        "count_report.csv"

    )




    df.to_csv(

        path,

        index=False

    )




    return {

        "message":

            "Report generated",


        "file":

            path,


        "records":

            len(df)

    }