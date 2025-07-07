class Movie:
    def __init__(self, title, genre):
        self.title = title
        self.genre = genre

    def to_dict(self):
        return {
            "title": self.title,
            "genre": self.genre
        }
    
    @classmethod
    def from_dict(cls, data):
        return cls(title=data["title"], genre=data["genre"])