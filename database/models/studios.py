from database.movie_db import no_return_query, insert_query, select_query

table_name = "studios"

def create_table_studios():
    query = f"""CREATE TABLE IF NOT EXISTS {table_name} (
    studio_id INTEGER PRIMARY KEY AUTOINCREMENT,
    studio_name TEXT UNIQUE,
    creation_date TEXT
    )"""
    no_return_query(query)

def insert_studio(studio):
    query = f"""INSERT INTO {table_name} (studio_id, studio_name, creation_date) 
    VALUES (?, ?, ?)"""
    p = (studio.studio_id, studio.studio_name, studio.creation_date)
    studio.studio_id = insert_query(query, p)