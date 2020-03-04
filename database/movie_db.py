import sqlite3

def open_connection():
    db_host = "movies.db"
    connection = sqlite3.connect(db_host)
    cursor = connection.cursor()
    return connection, cursor

def close_connection(connection):
    connection.close()


def no_return_query(query):
    try:
        connection, cursor = open_connection()
        cursor.execute(query)
        connection.commit()
    except sqlite3.DataError as error:
        print(error)
    finally:
        close_connection(connection)


def insert_query(query, p):
    try:
        connection, cursor = open_connection()
        cursor.execute(query, p)
        connection.commit()
        return cursor.lastrowid
    except sqlite3.DataError as error:
        print(error)
    finally:
        close_connection(connection)
    return None


def select_query(query, p = None):
    try:
        connection, cursor = open_connection()
        if p == None:
            cursor.execute(query)
        else:
            cursor.execute(query, p)
        return cursor.fetchall()
    except sqlite3.DataError as error:
        print(error)
    finally:
        close_connection(connection)
    return None


# # select_query("""SELECT movies.*, group_concat(actors.first_name ||\" \"|| actors.last_name ||\" - \"|| characters.character) FROM movies
# # JOIN characters ON movies.movie_id = characters.movie_id
# # JOIN actors ON characters.actor_id = actors.actor_id
# # GROUP BY movies.movie_id""")
# #
# # select_query("""SELECT movies.*, group_concat(writers.first_name || \" \" || writers.last_name) FROM movies
# # JOIN writing_crew ON movies.movie_id = writing_crew.movie_id
# # JOIN writers ON writing_crew.writer_id = writers.writer_id
# # GROUP BY movies.movie_id""")
#
# big = """SELECT studios.studio_name, studios.creation_date,
# directors.first_name, directors.last_name,
# group_concat(DISTINCT(writers.first_name || \" \" || writers.last_name)),
# movies.title, movies.language, movies.release_date, movies.runtime,
# group_concat(DISTINCT(actors.first_name ||\" \"|| actors.last_name ||\" - \"|| characters.character)),
# box_office.budget, box_office.gross
# FROM movies
# JOIN studios ON studios.studio_id = movies.studio_id
# JOIN directors ON directors.director_id = movies.director_id
# JOIN writing_crew ON writing_crew.movie_id = movies.movie_id
# JOIN writers ON writers.writer_id = writing_crew.writer_id
# JOIN characters ON characters.movie_id = movies.movie_id
# JOIN actors ON actors.actor_id = characters.actor_id
# JOIN box_office ON box_office.movie_id = movies.movie_id
# GROUP BY movies.movie_id
# """
# select_query(big)