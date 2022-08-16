import psycopg2
from sqlite_example import connect_to_sqlite
import queries
from pprint import pprint


dbname = 'srdhnafa'
host = 'ruby.db.elephantsql.com'
user = 'srdhnafa'
password = ''



def connect_to_pg():
    return psycopg2.connect(dbname=dbname, user=user, host=host, password=password)


def execute_query(conn, query):
    cursor = conn.cursor()
    cursor.execute(query)
    return cursor.fetchall()


def execute_ddl(conn, query):
    cursor = conn.cursor()
    cursor.execute(query)


def insert_character_data(conn, character_data):
    insert_query = f"""
    INSERT INTO character (
        character_id,
        name,
        level,
        exp,
        hp,
        strength,
        intelligence,
        dexterity,
        wisdom
    )
    VALUES
    {','.join([str(row) for row in character_data])}
    """
    execute_ddl(conn, insert_query)


if __name__ == '__main__':
    # connect to sqlite
    sqlite_conn = connect_to_sqlite()
    # query for character data
    character_data = execute_query(sqlite_conn, queries.select_all_characters)
    # connect to pg
    pg_conn = connect_to_pg()
    # create character table
    execute_ddl(pg_conn, queries.create_character_table)
    # insert the character data
    insert_character_data(pg_conn, character_data)
    # commit
    pg_conn.commit()