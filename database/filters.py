from database.movie_db import select_query

def filter_by_actor(actor_name, actor_surname):
    query = """SELECT movies.title, characters.character, actors.first_name, actors.last_name FROM actors
    JOIN characters ON characters.actor_id = actors.actor_id
    JOIN movies ON movies.movie_id = characters.movie_id
    WHERE actors.first_name = ? AND actors.last_name = ?"""
    p = (actor_name, actor_surname)
    return select_query(query, p)

def filter_by_character(role):
    q = """SELECT movies.title, movies.release_date, characters.character, actors.first_name, actors.last_name FROM characters
    JOIN actors ON actors.actor_id = characters.actor_id
    JOIN movies ON movies.movie_id = characters.movie_id
    WHERE characters.character = ?"""
    p = (role, )
    return select_query(q, p)

def filter_by_studio(studio_name):
    q = """SELECT studios.studio_name, movies.title, movies.release_date FROM studios
    JOIN movies ON movies.studio_id = studios.studio_id
    WHERE studios.studio_name = ?"""
    p = (studio_name, )
    return select_query(q, p)

def filter_by_movie_name(movie_title):
    q = """SELECT studios.studio_name, studios.creation_date, 
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
    WHERE movies.title = ?
    GROUP BY movies.movie_id
    """
    p = (movie_title, )
    return select_query(q, p)

def filter_by_director(first_name, last_name):
    q = """SELECT movies.release_date, movies.title, directors.first_name, directors.last_name FROM directors
    JOIN movies ON directors.director_id = movies.director_id
    WHERE directors.first_name = ? AND directors.last_name = ?"""
    p = (first_name, last_name)
    return select_query(q, p)

def filter_by_writer(first_name, last_name):
    q = """SELECT movies.release_date, movies.title, directors.first_name, directors.last_name, writers.first_name || \" \" || writers.last_name
    FROM writers
    JOIN writing_crew ON writing_crew.writer_id = writers.writer_id
    JOIN movies ON movies.movie_id = writing_crew.movie_id
    JOIN directors ON directors.director_id = movies.director_id
    WHERE writers.first_name = ? AND writers.last_name = ?"""
    p = (first_name, last_name)
    return select_query(q, p)

def filter_by_release_year(year):
    q = """SELECT movies.release_date, movies.title, movies.runtime, directors.first_name, directors.last_name, studios.studio_name
    FROM movies
    JOIN directors ON movies.director_id = directors.director_id
    JOIN studios ON movies.studio_id = studios.studio_id
    WHERE movies.release_date LIKE ?||'%'"""
    p = (year, )
    return select_query(q, p)

def filter_by_language(lang):
    q = """SELECT movies.release_date, movies.language, movies.title, movies.runtime, directors.first_name, directors.last_name
    FROM movies
    JOIN directors ON movies.director_id = directors.director_id
    WHERE movies.language = ? OR movies.language LIKE ?||'%'
    ORDER BY movies.release_date"""
    p = (lang, lang)
    return select_query(q, p)
