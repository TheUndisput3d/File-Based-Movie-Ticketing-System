from services.user_service import book_ticket, cancel_booking
from services.admin_service import add_showtime, add_movie
from data.data_store import *
from utils.input_handler import get_inputs, user_input_fields, shared_fields, admin_input_fields

def run():
    print("\nWelcome to the Movie Ticket Booking System")
    
    while True:
        role = input("\nAre you an 'Admin' or a 'User'?\nEnter 'admin', 'user', or 0 to exit: ").strip().lower()

        if role == "0":
            print("\nExiting the system. Have a great day!")
            break

        elif role == "admin":
            admin_data = get_inputs(admin_input_fields)
            movie_title = admin_data["movie_title"]
            genre = admin_data["genre"]
            time = admin_data["time"]
            seats = admin_data["seats"]
            add_movie(movie_title, genre)
            add_showtime(movie_title, time, seats)

        elif role == "user":
            user_data = get_inputs(user_input_fields)
            booking_id = book_ticket(
                user_data["user_name"],
                user_data["movie_title"],
                user_data["time"],
                user_data["seats"]
            )
            if booking_id:
                print(f"Booking Successful! ID: {booking_id}")
            else:
                print("Booking failed. Please check availability.")

        else:
            print("Invalid role. Please enter 'admin', 'user', or 0.")


if __name__ == "__main__":
    run()

