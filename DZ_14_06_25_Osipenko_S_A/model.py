import pickle
import os


class Films:
    def __init__(self, title, genre, author, year, duration, studio, actor):
        self.title = title
        self.genre = genre
        self.author = author
        self.year = year
        self.duration = duration
        self.studio = studio
        self.actor = actor

    def __str__(self):
        return f"{self.title} ({self.author})"


class FilmsModel:
    def __init__(self):
        self.db_name = "db.txt"
        self.films = self.load_data()

    def add_films(self, dict_films):
        films = Films(*dict_films.values())
        self.films[films.title] = films

    def get_all_films(self):
        return self.films.values()

    def get_single_films(self, user_title):
        films = self.films[user_title]
        dict_films = {
            "название фильма": films.title,
            "жанр": films.genre,
            "режиссер": films.author,
            "год выпуска": films.year,
            "длительность": films.duration,
            "студия": films.studio,
            "актеры": films.actor
        }
        return dict_films

    def remove_film(self, user_title):
        return self.films.pop(user_title)

    def save_data(self):
        with open(self.db_name, "wb") as f:
            pickle.dump(self.films, f)

    def load_data(self):
        if os.path.exists(self.db_name):
            with open(self.db_name, "rb") as f:
                return pickle.load(f)
        else:
            return {}
