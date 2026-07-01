import sqlite3
import os
from datetime import datetime


class Database:

    def __init__(self, path):

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

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            name TEXT NOT NULL,

            image TEXT,

            created TEXT

        )
        """)


        self.conn.execute("""
        CREATE TABLE IF NOT EXISTS count_events(

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            product_id INTEGER,

            track_id INTEGER,

            counted_at TEXT,

            FOREIGN KEY(product_id)
            REFERENCES products(id)

        )
        """)

        self.conn.execute("""
            CREATE TABLE IF NOT EXISTS cameras(

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            name TEXT NOT NULL,

            type TEXT,

            source TEXT NOT NULL,

            width INTEGER,

            height INTEGER,

            created TEXT

            )
        """)

        self.conn.commit()



    def add_product(
        self,
        name,
        image
    ):

        cursor = self.conn.execute(
            """
            INSERT INTO products
            (
                name,
                image,
                created
            )
            VALUES (?, ?, ?)
            """,
            (
                name,
                image,
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
                name,
                image,
                created

            FROM products

            ORDER BY id DESC

            """
        ).fetchall()


        products = []

        for row in rows:

            products.append({

                "id": row[0],

                "name": row[1],

                "image": row[2],

                "created": row[3]

            })


        return products
    
    def add_camera(
        self,
        name,
        type,
        source,
        width,
        height
    ):


        cursor = self.conn.execute(
        """
        INSERT INTO cameras
        (
            name,
            type,
            source,
            width,
            height,
            created
        )
        VALUES (?,?,?,?,?,?)
        """,
        (
            name,
            type,
            source,
            width,
            height,
            datetime.now().isoformat()
            )
        )


        self.conn.commit()


        return cursor.lastrowid





    def get_cameras(self):


        rows = self.conn.execute(
        """
        SELECT
        id,
        name,
        type,
        source,
        width,
        height
        FROM cameras
        """
        ).fetchall()



        return [

            {

            "id":r[0],
            "name":r[1],
            "type":r[2],
            "source":r[3],
            "width":r[4],
            "height":r[5]

            }

            for r in rows

        ]





    def get_camera(self,camera_id):


        row = self.conn.execute(
            """
            SELECT
            id,
            name,
            type,
            source,
            width,
            height
            FROM cameras
            WHERE id=?
        """,
        (camera_id,)
        ).fetchone()



        if not row:

            return None



        return {

        "id":row[0],

        "name":row[1],

        "type":row[2],

        "source":row[3],

        "width":row[4],

        "height":row[5]

        }




    def delete_camera(self,camera_id):


        self.conn.execute(
        """
        DELETE FROM cameras
        WHERE id=?
        """,
        (camera_id,)
        )


        self.conn.commit()


        return True