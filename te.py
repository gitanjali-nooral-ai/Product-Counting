import sqlite3

conn = sqlite3.connect("./data/database/app.db")

for table in ["products", "count_events"]:
    print("\nTABLE:", table)

    rows = conn.execute(
        f"PRAGMA table_info({table})"
    ).fetchall()

    for row in rows:
        print(row)