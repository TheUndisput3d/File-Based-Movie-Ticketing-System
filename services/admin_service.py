from data.data_store import movies, showtimes
from models.movie import Movie
from models.showtime import Showtime

def add_movie(title="Interstellar", genre="Sci-Fi"):
    movies.append(Movie(title, genre))

def add_showtime(movie_title, time, seats):
    movie = next((m for m in movies if m.title == movie_title), None)
    if movie:
        showtimes.append(Showtime(movie, time, seats))

        