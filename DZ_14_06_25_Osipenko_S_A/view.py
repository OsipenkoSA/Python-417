def add_title(title):
    def wrapper(func):
        def wrap(*args, **kwargs):
            print(f" {title} ".center(50, "="))
            output = func(*args, **kwargs)
            print("=" * 50)
            return output
        return wrap
    return wrapper


class UserInterface:
    @add_title("Редактирование данных каталога фильмов")
    def wait_user_answer(self):
        print("Действие с фильмами:")
        print("1 - Добавление фильма:"
              "\n2 - Каталог фильмов:"
              "\n3 - Просмотр определенного фильма"
              "\n4 - Удаление фильма"
              "\nq - Выход из программы")
        user_answer = input("Выберите вариант действия: ")
        return user_answer

    @add_title("Добавление фильма:")
    def add_user_film(self):
        dict_films = {
            "название фильма": None,
            "жанр": None,
            "режиссёр": None,
            "год выпуска": None,
            "длительность": None,
            "студия": None,
            "актеры": None
        }
        for key in dict_films:
            dict_films[key] = input(f"Введите {key}: ")
        return dict_films

    @add_title("Каталог фильмов:")
    def show_all_films(self, films):
        for ind, films in enumerate(films, 1):
            print(f"{ind}. {films}")

    @add_title("Ввод названия фильма:")
    def get_user_films(self):
        return input("Введите название фильма: ")

    @add_title("Просмотр определенного фильма:")
    def show_single_film(self, films):
        for key in films:
            print(f"{key} - {films[key]}")

    @add_title("Сообщение об ошибке:")
    def show_incorrect_title_error(self, user_title):
        print(f"Фильма с названием {user_title} не существует")

    @add_title("Удаление фильма:")
    def remove_single_films(self, films):
        print(f"Фильм {films} - был удален")

    @add_title("Сообщение об ошибке:")
    def show_incorrect_answer_error(self, answer):
        print(f"Варианта со значением {answer} не существует")
