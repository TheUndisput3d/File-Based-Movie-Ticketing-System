# Movie Ticket Booking System

A command-line based system that allows admins to manage movie showtimes and users to book tickets. Designed with modular components and **file-based JSON storage** for persistence and ease of testing.
---

## Features

###  Admin
- Add new movies with genres
- Schedule showtimes with specific timings and seat availability

### User
- View available movies and showtimes
- Book tickets for selected showtimes
- Cancel bookings using booking ID

---

## Project Structure

movie-ticket-booking/
│
├── data/
│   └── data_store.py         # Handles loading/saving data to JSON files
│   └── movies.json           # Stores movie data
│   └── showtimes.json        # Stores showtime data
│   └── bookings.json         # Stores booking data
│
├── models/
│   └── movie.py              # Movie class with serialization methods
│   └── showtime.py           # Showtime class with serialization methods
│   └── booking.py            # Booking class with serialization methods
│
├── services/
│   └── admin_service.py      # Admin operations: add movies and showtimes
│   └── user_service.py       # User operations: book and cancel tickets
│
├── utils/
│   └── input_handler.py      # Input validation and formatting
│
├── main.py                   # Entry point for running the system
└── README.md                 # Project documentation

## Data Persistence

All data is saved and loaded using JSON files for persistent storage:

- `data/movies.json`: Stores all added movies
- `data/showtimes.json`: Maintains scheduled showtimes and available seats
- `data/bookings.json`: Contains user booking records

This eliminates the need for temporary in-memory lists, allowing the system to retain state between sessions.

---

## Setup and Installation

To get the system up and running on your machine:

### 1. Clone the Repository

Use the following command to copy the project into your local system:

```bash
git clone <repository-url>
cd <repository-folder>

python main.py
```

### Python Version and Libraries Used

## Python Version: 3.10 or higher recommended
## Libraries Used:
- uuid - standard library for generating booking IDs
- Built-in functions and modules: input, print, list operations, etc
- No third-party libraries required


