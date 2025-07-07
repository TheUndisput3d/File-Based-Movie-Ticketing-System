shared_fields = {
    "movie_title": {
        "prompt": "Enter the movie title: ",
        "type": str,
        "format": str.title
    },
    "time": {
        "prompt": "Enter the showtime (e.g., '6:00PM'): ",
        "type": str,
        "format": lambda x: x.strip()
    },
    "seats": {
        "prompt": "Enter number of seats: ",
        "type": int,
        "format": lambda x: x
    }
}

admin_input_fields = {
    "genre": {
        "prompt": "Enter the genre of the movie: ",
        "type": str,
        "format": lambda x: x.strip().title()
    },
    **shared_fields
}

user_input_fields = {
    "user_name": {
        "prompt": "Enter your name: ",
        "type": str,
        "format": str.title
    },
    **shared_fields
}

def get_inputs(field_config):
    inputs = {}
    for key, spec in field_config.items():
        value = None
        while value is None:
            try:
                raw = input(spec["prompt"])
                casted = spec["type"](raw)
                value = spec["format"](casted)
            except Exception as e:
                print(f"Invalid input for {key}: {e}")
        inputs[key] = value
    return inputs


