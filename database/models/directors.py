from database.movie_db import no_return_query, insert_query, select_query

table_name = "directors"

def create_table_directors():
    query = f"""CREATE TABLE IF NOT EXISTS {table_name} (
    director_id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT,
    last_name TEXT
    )"""
    no_return_query(query)

def insert_director(director):
    query = f"""INSERT INTO {table_name} (director_id, first_name, last_name) 
    VALUES (?, ?, ?)"""
    p = (director.director_id, director.first_name, director.last_name)
    director.director_id = insert_query(query, p)