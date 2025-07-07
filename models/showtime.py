class Showtime:
    def __init__(self, movie="Interstellar", time="6:00PM", seats=100):
        self.movie = movie
        self.time = time
        self.seats = seats

    def to_dict(self):
        return {
            "movie": self.movie,
            "time": self.time,
            "seats": self.seats
        }
    
    @classmethod
    def from_dict(cls, data):
        return cls(
            movie=data["movie"],
            time=data["time"]
        )