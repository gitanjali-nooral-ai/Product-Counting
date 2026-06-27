import sqlite3
import os
from datetime import datetime



class Database:


    def __init__(self,path):


        folder = os.path.dirname(path)


        if folder:

            os.makedirs(
                folder,
                exist_ok=True
            )


        self.conn = sqlite3.connect(

            path,

            check_same_thread=False

        )


        self.create()





    def create(self):


        self.conn.execute("""

        CREATE TABLE IF NOT EXISTS products(

            id INTEGER PRIMARY KEY,

            name TEXT NOT NULL,

            image TEXT,

            model TEXT,

            created TEXT

        )

        """)



        self.conn.execute("""

        CREATE TABLE IF NOT EXISTS count_events(

            id INTEGER PRIMARY KEY,

            product_id INTEGER,

            track_id INTEGER,

            counted_at TEXT,

            FOREIGN KEY(product_id)

            REFERENCES products(id)

        )

        """)



        self.conn.commit()





    def add_product(
        self,
        name,
        image,
        model
    ):


        cursor = self.conn.execute(

            """

            INSERT INTO products

            (

                name,

                image,

                model,

                created

            )

            VALUES(?,?,?,?)

            """,

            (

                name,

                image,

                model,

                datetime.now().isoformat()

            )

        )

    
        self.conn.commit()

        return cursor.lastrowid

    def get_products(self):

        cursor = self.conn.cursor()

        rows = cursor.execute(
        """
        SELECT
            id,
            product_name,
            image_path,
            model_path,
            created_at
        FROM products
        ORDER BY id DESC
        """
        ).fetchall()


        return [

        {
            "id": row[0],
            "name": row[1],
            "image": row[2],
            "model": row[3],
            "created_at": row[4]
        }

            for row in rows

        ]

