from view import UserInterface
from model import FilmsModel


class Controller:
    def __init__(self):
        self.films_model = None
        self.user_interface = UserInterface()  # model
        self.films_model = FilmsModel()  # view

    def run(self):
        answer = None
        while answer != "q":
            answer = self.user_interface.wait_user_answer()
            self.check_user_answer(answer)

    def check_user_answer(self, answer):
        if answer == "1":
            films = self.user_interface.add_user_film()
            self.films_model.add_films(films)

        elif answer == "2":
            films = self.films_model.get_all_films()
            self.user_interface.show_all_films(films)

        elif answer == "3":
            films_title = self.user_interface.get_user_films()
            try:
                films = self.films_model.get_single_films(films_title)
            except KeyError:
                self.user_interface.show_incorrect_title_error(films_title)
            else:
                self.user_interface.show_single_film(films)

        elif answer == "4":
            films_title = self.user_interface.get_user_films()
            try:
                title = self.films_model.remove_film(films_title)
            except KeyError:
                self.user_interface.show_incorrect_title_error(films_title)
            else:
                self.user_interface.remove_single_films(title)

        elif answer == "q":
            self.films_model.save_data()

        else:
            self.user_interface.show_incorrect_answer_error(answer)
