import sqlite3
import queries
from pprint import pprint


def connect_to_sqlite(db_name="rpg_db.sqlite3"):
    # Connect to the db
    return sqlite3.connect("rpg_db.sqlite3")


def execute_query(conn, query):
    # Make a cursor (a middle man)
    cursor = conn.cursor()
    # Execute our query
    cursor.execute(query)
    # Pull results from the cursor
    results = cursor.fetchall()
    return results


if __name__ == '__main__':
    conn = connect_to_sqlite()
    results = execute_query(conn, queries.total_characters)
    pprint(results)
