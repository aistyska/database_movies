from database.movie_db import no_return_query, insert_query, select_query

table_name = "box_office"

def create_box_office():
    query = f"""CREATE TABLE IF NOT EXISTS {table_name} (
    box_office_id INTEGER PRIMARY KEY AUTOINCREMENT,
    budget INTEGER,
    gross INTEGER,
    movie_id INTEGER,
    FOREIGN KEY (movie_id) REFERENCES movies(movie_id)
    )"""
    no_return_query(query)


def insert_box_office(box_office):
    query = f"""INSERT INTO {table_name} (box_office_id, budget, gross, movie_id)
    VALUES (?, ?, ?, ?)"""
    p = (box_office.box_office_id, box_office.budget, box_office.gross, box_office.movie_id)
    box_office.box_office_id = insert_query(query, p)



