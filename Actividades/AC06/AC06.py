from datetime import datetime as dt
from functools import reduce


def set_id():
    a = 0
    while True:
        yield a
        a += 1


class Cast:
    def __init__(self, movie_title, name, character):
        self.name = name
        self.movie = movie_title
        self.character = character

    def __repr__(self):
        return self.name


class Movie:
    get_id = set_id()

    def __init__(self, title, rating, release, *args):
        self.id = next(Movie.get_id)
        self.title = title
        self.rating = float(rating)
        self.release = dt.strptime(release, '%Y-%m-%d')  # 2015-03-04
        self.genres = [arg for arg in args]

    def __repr__(self):
        return self.title


def popular(valor):
    lista_rating = []
    lista = [lista_rating.append(p) for p in lista_peliculas if p.rating > valor]
    return lista_rating


def with_genres(*args):
    pass


def tops_of_genre():
    pass


def actor_rating(actor):
    actorsh = [a for a in lista_cast if a.name == actor]
    peliculas = [a.movie for a in actorsh]
    rating = [peli for peli in lista_peliculas if peli.title in peliculas]
    total = [peli.rating for peli in rating]
    a = reduce(lambda x,y: (x+y)/len(total), total)
    return a


def compare_actors(actor1, actor2):
    if actor_rating(actor1) > actor_rating(actor2):
        return actor1
    else:
        return actor2


def movies_of(actor):
    pelis = [a.movie for a in lista_cast if a.name == actor]
    personajes = [a.character for a in lista_cast if a.name == actor]
    a = zip(pelis,personajes)
    lista = [v for v in a]
    return lista


def from_year(year):
    lista_dada = [a for a in lista_peliculas if a.year == year]
    return lista_dada


if __name__ == "__main__":
    with open('movies.txt', 'r') as f:
        lista_peliculas = []
        p = map(lambda x: x.split(","), f)
        p = [lista_peliculas.append(Movie(a[1], a[2], a[3], a[4])) for a in p]

    with open('cast.txt', 'r') as f:
        lista_cast =[]
        p = map(lambda x: x.split(","), f)
        p = [lista_cast.append(Cast(a[0], a[1], a[2])) for a in p]

