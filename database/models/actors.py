from database.movie_db import no_return_query, insert_query, select_query

table_name = "actors"

def create_table_actors():
    query = f"""CREATE TABLE IF NOT EXISTS {table_name} (
    actor_id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT,
    last_name TEXT
    )"""
    no_return_query(query)

def insert_actor(actor):
    query = f"""INSERT INTO {table_name} (actor_id, first_name, last_name) 
    VALUES (?, ?, ?)"""
    p = (actor.actor_id, actor.first_name, actor.last_name)
    actor.actor_id = insert_query(query, p)
