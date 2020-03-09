from objects.actor import Actor
from objects.box_office import Box_office
from objects.character import Character
from objects.director import Director
from objects.movie import Movie
from objects.studio import Studio
from objects.writer import Writer
from objects.writing_crew import Crew

from database.models.actors import create_table_actors, insert_actor
from database.models.box_offices import create_box_office, insert_box_office
from database.models.characters import create_table_characters, insert_character
from database.models.directors import create_table_directors, insert_director
from database.models.movies import create_table_movies, insert_movie, update_movie, select_everything
from database.models.studios import create_table_studios, insert_studio
from database.models.writers import create_table_writers, insert_writer
from database.models.writing_crews import create_table_writing_crew, insert_writing_crew


import database.filters as filters

def print_results(result):
    for line in result:
        print(line)

create_table_movies()
create_table_actors()
create_table_characters()
create_table_writers()
create_table_writing_crew()
create_table_directors()
create_table_studios()
create_box_office()

d1 = Director(None, "Sam", "Mendes")
insert_director(d1)

s1 = Studio(None, "Columbia Pictures", 1924)
insert_studio(s1)

m1 = Movie(None, "Spectre", "English", "2015-11-6", 148, d1.director_id, s1.studio_id, None)
insert_movie(m1)

b1 = Box_office(None, 245000000, 200074609, m1.movie_id)
insert_box_office(b1)

m1.box_office_id = b1.box_office_id
update_movie(m1)

a1 = Actor(None, "Daniel", "Craig")
insert_actor(a1)
a2 = Actor(None, "Christoph", "Waltz")
insert_actor(a2)
a3 = Actor(None, "Lea", "Seydoux")
insert_actor(a3)

ch1 = Character(None, "James Bond", a1.actor_id, m1.movie_id)
insert_character(ch1)
ch2 = Character(None, "Blofeld", a2.actor_id, m1.movie_id)
insert_character(ch2)
ch3 = Character(None, "Madeleine", a3.actor_id, m1.movie_id)
insert_character(ch3)

w1 = Writer(None, "John", "Logan")
insert_writer(w1)
w2 = Writer(None, "Neal", "Purvis")
insert_writer(w2)
w3 = Writer(None, "Robert", "Wade")
insert_writer(w3)
w4 = Writer(None, "Jez", "Butterworth")
insert_writer(w4)

wc1 = Crew(None, w1.writer_id, m1.movie_id)
insert_writing_crew(wc1)
wc2 = Crew(None, w2.writer_id, m1.movie_id)
insert_writing_crew(wc2)
wc3 = Crew(None, w3.writer_id, m1.movie_id)
insert_writing_crew(wc3)
wc4 = Crew(None, w4.writer_id, m1.movie_id)
insert_writing_crew(wc4)




m2 = Movie(None, "Skyfall", "English", "2012-11-9", 143, d1.director_id, s1.studio_id, None)
insert_movie(m2)

b2 = Box_office(None, 200000000, 30430277, m2.movie_id)
insert_box_office(b2)

m2.box_office_id = b2.box_office_id
update_movie(m2)

a4 = Actor(None, "Judi", "Dench")
insert_actor(a4)
a5 = Actor(None, "Javier", "Bardem")
insert_actor(a5)
a6 = Actor(None, "Ralph", "Fiennes")
insert_actor(a6)

ch4 = Character(None, "James Bond", a1.actor_id, m2.movie_id)
insert_character(ch4)
ch5 = Character(None, "M", a4.actor_id, m2.movie_id)
insert_character(ch5)
ch6 = Character(None, "Silva", a5.actor_id, m2.movie_id)
insert_character(ch6)
ch7 = Character(None, "Gareth Mallory", a6.actor_id, m2.movie_id)
insert_character(ch7)

w5 = Writer(None, "Ian", "Fleming")
insert_writer(w5)

wc5 = Crew(None, w2.writer_id, m2.movie_id)
insert_writing_crew(wc5)
wc6 = Crew(None, w3.writer_id, m2.movie_id)
insert_writing_crew(wc6)
wc7 = Crew(None, w1.writer_id, m2.movie_id)
insert_writing_crew(wc7)
wc8 = Crew(None, w5.writer_id, m2.movie_id)
insert_writing_crew(wc8)

d2 = Director(None, "Rian", "Johnson")
insert_director(d2)

s2 = Studio(None, "Lionsgate", 1997)
insert_studio(s2)

m3 = Movie(None, "Knives Out", "English", "2019-11-27", 131, d2.director_id, s2.studio_id, None)
insert_movie(m3)

b3 = Box_office(None, 40000000, 163708563, m3.movie_id)
insert_box_office(b3)

m3.box_office_id = b3.box_office_id
update_movie(m3)

a7 = Actor(None, "Chris", "Evans")
insert_actor(a7)
a8 = Actor(None, "Ana", "de Armas")
insert_actor(a8)
a9 = Actor(None, "Jamie Lee", "Curtis")
insert_actor(a9)

ch8 = Character(None, "Benoit Blanc", a1.actor_id, m3.movie_id)
insert_character(ch8)
ch9 = Character(None, "Ransom Drysdale", a7.actor_id, m3.movie_id)
insert_character(ch9)
ch10 = Character(None, "Marta Cabrera", a8.actor_id, m3.movie_id)
insert_character(ch10)
ch11 = Character(None, "Linda Drysdale", a9.actor_id, m3.movie_id)
insert_character(ch11)

w9 = Writer(None, "Rian", "Johnson")
insert_writer(w9)

wc9 = Crew(None, w9.writer_id, m3.movie_id)
insert_writing_crew(wc9)

everything = select_everything()
print_results(everything)


print_results(filters.filter_by_actor("Daniel", "Craig"))
print_results(filters.filter_by_character("James Bond"))
print_results(filters.filter_by_studio("Columbia Pictures"))
print_results(filters.filter_by_movie_name("Skyfall"))
print_results(filters.filter_by_director("Rian", "Johnson"))
print_results(filters.filter_by_writer("John", "Logan"))
print_results(filters.filter_by_release_year("2012"))
print_results(filters.filter_by_language("En"))