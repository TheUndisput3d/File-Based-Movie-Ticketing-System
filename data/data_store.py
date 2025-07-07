# movies = []
# showtimes = []
# bookings = []

import os
import json

movie_file = "data/movies.json"
showtime_file = "data/showtimes.json"
booking_file = "data/bookings.json"

def load_data(file):
    if os.path.exists(file):
        with open(file, "r") as f:
            return json.load(f)
    return []

def save_data(file, data):
    with open(file, "w") as f:
        json.dump(data, f, indent=4)

movies = load_data(movie_file)
showtimes = load_data(showtime_file)
bookings = load_data(booking_file)

