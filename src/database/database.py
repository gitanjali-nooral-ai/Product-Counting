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