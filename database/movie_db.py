import sqlite3
from objects.actor import Actor
from objects.box_office import Box_office
from objects.character import Character
from objects.director import Director
from objects.movie import Movie
from objects.studio import Studio
from objects.writer import Writer
from objects.writing_crew import Crew

def open_connection():
    db_host = "movies.db"
    connection = sqlite3.connect(db_host)
    cursor = connection.cursor()
    return connection, cursor


def close_connection(connection):
    connection.close()


def table_query(query):
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
        for row in cursor:
            print(row)
    except sqlite3.DataError as error:
        print(error)
    finally:
        close_connection(connection)


def create_table_movies():
    query ="""CREATE TABLE IF NOT EXISTS movies (
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
    table_query(query)

def create_table_directors():
    query = """CREATE TABLE IF NOT EXISTS directors (
    director_id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT,
    last_name TEXT
    )"""
    table_query(query)

def create_table_studios():
    query = """CREATE TABLE IF NOT EXISTS studios (
    studio_id INTEGER PRIMARY KEY AUTOINCREMENT,
    studio_name TEXT UNIQUE,
    creation_date TEXT
    )"""
    table_query(query)

def create_box_office():
    query = """CREATE TABLE IF NOT EXISTS box_office (
    box_office_id INTEGER PRIMARY KEY AUTOINCREMENT,
    budget INTEGER,
    gross INTEGER,
    movie_id INTEGER,
    FOREIGN KEY (movie_id) REFERENCES movies(movie_id)
    )"""
    table_query(query)

def create_table_actors():
    query = """CREATE TABLE IF NOT EXISTS actors (
    actor_id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT,
    last_name TEXT
    )"""
    table_query(query)

def create_table_characters():
    query = """CREATE TABLE IF NOT EXISTS characters (
    role_id INTEGER PRIMARY KEY AUTOINCREMENT,
    character TEXT,
    actor_id INTEGER,
    movie_id INTEGER,
    FOREIGN KEY (actor_id) REFERENCES actors(actor_id),
    FOREIGN KEY (movie_id) REFERENCES movies(movie_id)
    )"""
    table_query(query)

def create_table_writers():
    query = """CREATE TABLE IF NOT EXISTS writers(
    writer_id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT,
    last_name TEXT
    )"""
    table_query(query)

def create_table_writing_crew():
    query = """CREATE TABLE IF NOT EXISTS writing_crew (
    crew_id INTEGER PRIMARY KEY AUTOINCREMENT,
    writer_id INTEGER,
    movie_id INTEGER,
    FOREIGN KEY (writer_id) REFERENCES writers(writer_id),
    FOREIGN KEY (movie_id) REFERENCES movies(movie_id)
    )"""
    table_query(query)

def insert_director(director):
    query = """INSERT INTO directors (director_id, first_name, last_name) 
    VALUES (?, ?, ?)"""
    p = (director.director_id, director.first_name, director.last_name)
    director.director_id = insert_query(query, p)

def insert_studio(studio):
    query = """INSERT INTO studios (studio_id, studio_name, creation_date) 
    VALUES (?, ?, ?)"""
    p = (studio.studio_id, studio.studio_name, studio.creation_date)
    studio.studio_id = insert_query(query, p)

def insert_actor(actor):
    query = """INSERT INTO actors (actor_id, first_name, last_name) 
    VALUES (?, ?, ?)"""
    p = (actor.actor_id, actor.first_name, actor.last_name)
    actor.actor_id = insert_query(query, p)

def insert_writer(writer):
    query = """INSERT INTO writers (writer_id, first_name, last_name)
    VALUES (?, ?, ?)"""
    p = (writer.writer_id, writer.first_name, writer.last_name)
    writer.writer_id = insert_query(query, p)

def insert_writing_crew(crew):
    query = """INSERT INTO writing_crew (crew_id, writer_id, movie_id)
    VALUES (?, ?, ?)"""
    p = (crew.crew_id, crew.writer_id, crew.movie_id)
    crew.crew_id = insert_query(query, p)

def insert_character(character):
    query = """INSERT INTO characters (role_id, character, actor_id, movie_id)
    VALUES (?, ?, ?, ?)"""
    p = (character.role_id, character.character, character.actor_id, character.movie_id)
    character.role_id = insert_query(query, p)

def insert_movie_and_box_office(movie, box_office):
    try:
        connection, cursor = open_connection()

        query_movie = """INSERT INTO movies (movie_id, title, language, release_date, runtime, director_id, studio_id, box_office_id) 
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)"""
        p_for_movie = (movie.movie_id, movie.title, movie.language, movie.release_date, movie.runtime, movie.director_id, movie.studio_id, movie.box_office_id)
        cursor.execute(query_movie, p_for_movie)
        movie.movie_id = cursor.lastrowid
        connection.commit()

        query_box_office = """INSERT INTO box_office (box_office_id, budget, gross, movie_id)
        VALUES (?, ?, ?, ?)"""
        p_for_box = (box_office.box_office_id, box_office.budget, box_office.gross, movie.movie_id)
        cursor.execute(query_box_office, p_for_box)
        box_office.box_office_id = cursor.lastrowid
        connection.commit()

        q_update_movie = """UPDATE movies SET box_office_id = ?
        WHERE movie_id = ?"""
        p_for_update = (box_office.box_office_id, movie.movie_id)
        cursor.execute(q_update_movie, p_for_update)
        connection.commit()

    except sqlite3.DataError as error:
        print(error)
    finally:
        close_connection(connection)


create_table_movies()
create_table_actors()
create_table_characters()
create_table_writers()
create_table_writing_crew()
create_table_directors()
create_table_studios()
create_box_office()


d = Director(None, "Sam", "Mendes")
insert_director(d)
s = Studio(None, "Columbia Pictures", 1924)
insert_studio(s)
b = Box_office(None, 245000000, 200074609, None)
m = Movie(None, "Spectre", "English", "2015-11-6", 148, d.director_id, s.studio_id, None)
insert_movie_and_box_office(m, b)
a1 = Actor(None, "Daniel", "Craig")
insert_actor(a1)
a2 = Actor(None, "Christoph", "Waltz")
insert_actor(a2)
a3 = Actor(None, "Lea", "Seydoux")
insert_actor(a3)
ch1 = Character(None, "James Bond", a1.actor_id, m.movie_id)
insert_character(ch1)
ch2 = Character(None, "Blofeld", a2.actor_id, m.movie_id)
insert_character(ch2)
ch3 = Character(None, "Madeleine", a3.actor_id, m.movie_id)
insert_character(ch3)
w1 = Writer(None, "John", "Logan")
insert_writer(w1)
w2 = Writer(None, "Neal", "Purvis")
insert_writer(w2)
w3 = Writer(None, "Robert", "Wade")
insert_writer(w3)
w4 = Writer(None, "Jez", "Butterworth")
insert_writer(w4)
wc1 = Crew(None, w1.writer_id, m.movie_id)
insert_writing_crew(wc1)
wc2 = Crew(None, w2.writer_id, m.movie_id)
insert_writing_crew(wc2)
wc3 = Crew(None, w3.writer_id, m.movie_id)
insert_writing_crew(wc3)
wc4 = Crew(None, w4.writer_id, m.movie_id)
insert_writing_crew(wc4)


b1 = Box_office(None, 200000000, 30430277, None)
m1 = Movie(None, "Skyfall", "English", "2012-11-9", 143, d.director_id, s.studio_id, None)
insert_movie_and_box_office(m1, b1)

a4 = Actor(None, "Judi", "Dench")
insert_actor(a4)
a5 = Actor(None, "Javier", "Bardem")
insert_actor(a5)
a6 = Actor(None, "Ralph", "Fiennes")
insert_actor(a6)

ch4 = Character(None, "James Bond", a1.actor_id, m1.movie_id)
insert_character(ch4)
ch5 = Character(None, "M", a4.actor_id, m1.movie_id)
insert_character(ch5)
ch6 = Character(None, "Silva", a5.actor_id, m1.movie_id)
insert_character(ch6)
ch7 = Character(None, "Gareth Mallory", a6.actor_id, m1.movie_id)
insert_character(ch7)

w5 = Writer(None, "Ian", "Fleming")
insert_writer(w5)

wc5 = Crew(None, w2.writer_id, m1.movie_id)
insert_writing_crew(wc5)
wc6 = Crew(None, w3.writer_id, m1.movie_id)
insert_writing_crew(wc6)
wc7 = Crew(None, w1.writer_id, m1.movie_id)
insert_writing_crew(wc7)
wc8 = Crew(None, w5.writer_id, m1.movie_id)
insert_writing_crew(wc8)


d1 = Director(None, "Rian", "Johnson")
insert_director(d1)

s1 = Studio(None, "Lionsgate", 1997)
insert_studio(s1)

m2 = Movie(None, "Knives Out", "English", "2019-11-27", 131, d1.director_id, s1.studio_id, None)
b2 = Box_office(None, 40000000, 163708563, None)
insert_movie_and_box_office(m2, b2)

a7 = Actor(None, "Chris", "Evans")
insert_actor(a7)
a8 = Actor(None, "Ana", "de Armas")
insert_actor(a8)
a9 = Actor(None, "Jamie Lee", "Curtis")
insert_actor(a9)

ch8 = Character(None, "Benoit Blanc", a1.actor_id, m2.movie_id)
insert_character(ch8)
ch9 = Character(None, "Ransom Drysdale", a7.actor_id, m2.movie_id)
insert_character(ch9)
ch10 = Character(None, "Marta Cabrera", a8.actor_id, m2.movie_id)
insert_character(ch10)
ch11 = Character(None, "Linda Drysdale", a9.actor_id, m2.movie_id)
insert_character(ch11)

w9 = Writer(None, "Rian", "Johnson")
insert_writer(w9)
wc9 = Crew(None, w9.writer_id, m2.movie_id)
insert_writing_crew(wc9)


# select_query("""SELECT movies.*, group_concat(actors.first_name ||\" \"|| actors.last_name ||\" - \"|| characters.character) FROM movies
# JOIN characters ON movies.movie_id = characters.movie_id
# JOIN actors ON characters.actor_id = actors.actor_id
# GROUP BY movies.movie_id""")
#
# select_query("""SELECT movies.*, group_concat(writers.first_name || \" \" || writers.last_name) FROM movies
# JOIN writing_crew ON movies.movie_id = writing_crew.movie_id
# JOIN writers ON writing_crew.writer_id = writers.writer_id
# GROUP BY movies.movie_id""")

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
select_query(big)