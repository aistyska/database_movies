from database.movie_db import no_return_query, insert_query, select_query

table_name = "movies"

def create_table_movies():
    query = f"""CREATE TABLE IF NOT EXISTS {table_name} (
    movie_id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT,
    language TEXT,
    release_date TEXT,
    runtime INTEGER,
    director_id INTEGER,
    studio_id INTEGER,
    box_office_id INTEGER,
    FOREIGN KEY (director_id) REFERENCES directors(director_id),
    FOREIGN KEY (studio_id) REFERENCES studios(studio_id), 
    FOREIGN KEY (box_office_id) REFERENCES box_office(box_office_id)
    )"""
    no_return_query(query)


def insert_movie(movie):
    query = f"""INSERT INTO {table_name} (movie_id, title, language, release_date, runtime, director_id, studio_id, box_office_id) 
    VALUES (?, ?, ?, ?, ?, ?, ?, ?)"""
    p  = (movie.movie_id, movie.title, movie.language, movie.release_date, movie.runtime, movie.director_id, movie.studio_id,
    movie.box_office_id)
    movie.movie_id = insert_query(query, p)


def update_movie(movie):
    q = f"""UPDATE {table_name} SET box_office_id = ?
    WHERE movie_id = ?"""
    p = (movie.box_office_id, movie.movie_id)
    insert_query(q, p)



def select_everything():
    big = """SELECT studios.studio_name, studios.creation_date, 
    directors.first_name, directors.last_name,
    group_concat(DISTINCT(writers.first_name || \" \" || writers.last_name)),
    movies.title, movies.language, movies.release_date, movies.runtime,
    group_concat(DISTINCT(actors.first_name ||\" \"|| actors.last_name ||\" - \"|| characters.character)),
    box_office.budget, box_office.gross
    FROM movies
    JOIN studios ON studios.studio_id = movies.studio_id
    JOIN directors ON directors.director_id = movies.director_id
    JOIN writing_crew ON writing_crew.movie_id = movies.movie_id
    JOIN writers ON writers.writer_id = writing_crew.writer_id
    JOIN characters ON characters.movie_id = movies.movie_id
    JOIN actors ON actors.actor_id = characters.actor_id
    JOIN box_office ON box_office.movie_id = movies.movie_id
    GROUP BY movies.movie_id
    """
    return select_query(big)
