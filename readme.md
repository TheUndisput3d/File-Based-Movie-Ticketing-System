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

## Data Persistence

All data is saved and loaded using JSON files for persistent storage:

- `data/movies.json`: Stores all added movies
- `data/showtimes.json`: Maintains scheduled showtimes and available seats
- `data/bookings.json`: Contains user booking records

This eliminates the need for temporary in-memory lists, allowing the system to retain state between sessions.

---

## Modules Overview

### `data_store.py`
Handles reading and writing JSON files for movies, showtimes, and bookings.

### `movie.py`, `showtime.py`, `booking.py`
Each model includes:
- Constructor
- `to_dict()` for serialization
- `from_dict()` for deserialization

### `admin_service.py`
- `add_movie(title, genre)`
- `add_showtime(movie_title, time, seats)`

### `user_service.py`
- `book_ticket(user_name, movie_title, time, seats)`
- `cancel_booking(booking_id)`

### `input_handler.py`
Reusable input prompts and validation for both admin and user roles.

### `main.py`
Main loop for role selection and interaction.

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


