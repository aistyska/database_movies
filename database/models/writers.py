from database.movie_db import no_return_query, insert_query, select_query

table_name = "writers"

def create_table_writers():
    query = f"""CREATE TABLE IF NOT EXISTS {table_name} (
    writer_id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT,
    last_name TEXT
    )"""
    no_return_query(query)

def insert_writer(writer):
    query = f"""INSERT INTO {table_name} (writer_id, first_name, last_name)
    VALUES (?, ?, ?)"""
    p = (writer.writer_id, writer.first_name, writer.last_name)
    writer.writer_id = insert_query(query, p)