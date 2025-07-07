import uuid

class Booking:
    def __init__(self, user_name, movie, time, seats_booked):
        self.id = str(uuid.uuid4())
        self.user_name = user_name
        self.movie = movie
        self.time = time
        self.seats_booked = seats_booked
        
    def to_dict(self):
        return {
            "id": self.id,
            "user_name": self.user_name,
            "movie": self.movie,
            "time": self.time, 
            "seats_booked": self.seats_booked
        }
    
    @classmethod
    def from_dict(cls, data):
        obj = cls(
            user_name=data["user_name"],
            movie=data["movie"],
            time=data["time"],
            seats_booked=data["seats_booked"]
        )
        obj.id = data["id"]  
        return obj
