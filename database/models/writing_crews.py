from database.movie_db import no_return_query, insert_query, select_query

table_name = "writing_crew"

def create_table_writing_crew():
    query = f"""CREATE TABLE IF NOT EXISTS {table_name} (
    crew_id INTEGER PRIMARY KEY AUTOINCREMENT,
    writer_id INTEGER,
    movie_id INTEGER,
    FOREIGN KEY (writer_id) REFERENCES writers(writer_id),
    FOREIGN KEY (movie_id) REFERENCES movies(movie_id)
    )"""
    no_return_query(query)

def insert_writing_crew(crew):
    query = f"""INSERT INTO {table_name} (crew_id, writer_id, movie_id)
    VALUES (?, ?, ?)"""
    p = (crew.crew_id, crew.writer_id, crew.movie_id)
    crew.crew_id = insert_query(query, p)