from database.movie_db import no_return_query, insert_query, select_query

table_name = "characters"

def create_table_characters():
    query = f"""CREATE TABLE IF NOT EXISTS {table_name} (
    role_id INTEGER PRIMARY KEY AUTOINCREMENT,
    character TEXT,
    actor_id INTEGER,
    movie_id INTEGER,
    FOREIGN KEY (actor_id) REFERENCES actors(actor_id),
    FOREIGN KEY (movie_id) REFERENCES movies(movie_id)
    )"""
    no_return_query(query)


def insert_character(character):
    query = f"""INSERT INTO {table_name} (role_id, character, actor_id, movie_id)
    VALUES (?, ?, ?, ?)"""
    p = (character.role_id, character.character, character.actor_id, character.movie_id)
    character.role_id = insert_query(query, p)