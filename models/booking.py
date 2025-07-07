import uuid
class Booking:
    def __init__(self, user_name, movie, time, seats_booked):
        self.id = str(uuid.uuid4())
        self.user_name = user_name
        self.movie = movie
        self.time = time
        self.seats_booked = seats_booked
        
