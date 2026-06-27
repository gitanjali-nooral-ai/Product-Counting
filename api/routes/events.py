from fastapi import APIRouter, Query

from src.database.database import Database
from config.settings import settings


router = APIRouter(
    prefix="/events",
    tags=["Events"]
)


database = Database(
    settings.database["path"]
)



@router.get("/")
def get_events(
    limit: int = Query(
        50,
        ge=1,
        le=500
    )
):

    cursor = database.conn.cursor()


    rows = cursor.execute(
        """

        SELECT

            count_events.id,

            count_events.product_id,

            products.name,

            count_events.counted_at


        FROM count_events


        LEFT JOIN products

        ON products.id = count_events.product_id


        ORDER BY count_events.id DESC


        LIMIT ?

        """,

        (limit,)

    ).fetchall()



    events = []


    for row in rows:

        events.append({

            "event_id": row[0],

            "product_id": row[1],

            "product_name": row[2] if row[2] else "Unknown",

            "counted_at": row[3]

        })


    return {

        "total": len(events),

        "events": events

    }