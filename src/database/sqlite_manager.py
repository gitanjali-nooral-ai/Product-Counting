import sqlite3
import os
from datetime import datetime



class Database:


    def __init__(

        self,

        path

    ):


        os.makedirs(

            os.path.dirname(path),

            exist_ok=True

        )


        self.conn=sqlite3.connect(

            path,

            check_same_thread=False

        )


        self.create_tables()



    def create_tables(self):


        cursor=self.conn.cursor()



        cursor.execute("""

        CREATE TABLE IF NOT EXISTS products(

            id INTEGER PRIMARY KEY,

            product_name TEXT,

            image_path TEXT,

            embedding_path TEXT,

            created_at TEXT

        )

        """)



        cursor.execute("""

        CREATE TABLE IF NOT EXISTS count_events(

            id INTEGER PRIMARY KEY,

            product_id INTEGER,

            track_id INTEGER,

            counted_at TEXT

        )

        """)


        self.conn.commit()



    def add_product(

        self,

        name,

        image,

        embedding

    ):


        cur=self.conn.cursor()


        cur.execute(

        """

        INSERT INTO products

        (

        product_name,

        image_path,

        embedding_path,

        created_at

        )

        VALUES(?,?,?,?)

        """,

        (

        name,

        image,

        embedding,

        datetime.now().isoformat()

        ))


        self.conn.commit()


        return cur.lastrowid



    def add_count(

        self,

        product_id,

        track_id

    ):


        self.conn.execute(

        """

        INSERT INTO count_events

        VALUES(NULL,?,?,?)

        """,

        (

        product_id,

        track_id,

        datetime.now().isoformat()

        ))


        self.conn.commit()



    def get_products(self):


        cur=self.conn.cursor()


        return cur.execute(

        """

        SELECT id,product_name

        FROM products

        """

        ).fetchall()