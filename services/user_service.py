from data.data_store import bookings, showtimes
from models.booking import Booking

def book_ticket(user_name, movie_title, time, seats):
    for s in showtimes:
        if s.movie.title == movie_title and s.time == time:
            if s.seats >= seats:
                s.seats -= seats
                booking = Booking(user_name, movie_title, time, seats)
                bookings.append(booking)
                return booking.id
    return None

def cancel_booking(booking_id):
    for b in bookings:
        if b.id == booking_id:
            bookings.remove(b)
            for s in showtimes:
                if s.movie.title == b.movie and s.time == b.time:
                    s.seats += b.seats_booked
                    break
            return True
    return False



