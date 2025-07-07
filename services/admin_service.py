from data.data_store import movies, showtimes, save_data, movie_file, showtime_file
from models.movie import Movie
from models.showtime import Showtime

def add_movie(title="Interstellar", genre="Sci-Fi"):
    movie = Movie(title, genre)
    movies.append(movie.to_dict())
    save_data(movie_file, movies)

def add_showtime(movie_title, time, seats):
    movie_obj = next(
    (Movie.from_dict(m) for m in movies if m["title"] == movie_title),
    None
)

    if movie_obj:
        showtime = Showtime(movie_obj.to_dict(), time, seats)
        showtimes.append(showtime.to_dict())
        save_data(showtime_file, showtimes)

        