from tools.exceptions.book_exc import BookNotFoundError
from tools.models.console_color import Color
from tools.reader.json_reader import FileReader
from tools.writer.json_writer import FileWriter


class App:
    """
    Main app. Contains the processing of user input
    and the application menu
    """

    def __init__(self):
        self.reader = FileReader()
        self.writer = FileWriter()
        self.menu_point = {
            '1': self.show_all_books,
            '2': self.processing_find_books,
            '3': self.processing_add_book,
            '4': self.processing_edit_status,
            '5': self.processing_delete_book
        }
        self.sub_find_menu = {
            '1': self.reader.search_books_by_author,
            '2': self.reader.search_books_by_title,
            '3': self.reader.search_books_by_year
        }

    def check_year(self, year: str) -> str:
        try:
            year = int(year)
            if year <= 0:
                return f'{Color.RED.value}Год должен быть больше чем 0{Color.RESET.value}'
        except ValueError as ex:
            return f'{Color.RED.value}Год должен быть целым числом {Color.RESET.value}'

        return 'valid'

    def get_main_menu(self) -> str:
        return (f"Главное меню\n"
                f"(1) Просмотреть все книги\n"
                f"(2) Найти книги\n"
                f"(3) Добавить книгу\n"
                f"(4) Изменить статус книги\n"
                f"(5) Удалить книгу\n"
                f"(-1) {Color.RED.value}Выход{Color.RESET.value}")

    def show_all_books(self) -> None:
        try:
            books = self.reader.get_all()
        except FileNotFoundError as ex:
            print(f'{Color.RED.value}{str(ex)}{Color.RESET.value}')
            return

        if len(books) == 0:
            print(f'{Color.YELLOW.value}В библиотеке нет книг{Color.RESET.value}')
            return

        print(f'{Color.BLUE.value}Все книги{Color.RESET.value}')

        for book in books:
            print(book)
        print()

    def processing_find_books(self) -> None:
        sub_menu = {
            '1': 'автора',
            '2': 'название',
            '3': 'год'
        }

        print(f"{Color.MAGENTA.value}Поиск книги{Color.RESET.value}\n"
              f"Выберите поле для поиска\n"
              f"(1) Автор\n"
              f"(2) Название\n"
              f"(3) Год издания\n"
              f"(-1) Выход в главное меню")

        while True:
            choice = input('-> ')

            if choice == '-1':
                return

            try:
                param = input(f"Введите {sub_menu[choice]} -> ")

                if choice == '3':
                    result = self.check_year(param)

                    if result != 'valid':
                        print(result)
                        print("Выберите поле для поиска")
                        continue
                    else:
                        param = int(param)

                books = self.sub_find_menu[choice](param)

                if len(books) > 0:
                    for book in books:
                        print(book)
                else:
                    print(f'{Color.YELLOW.value}Книги не найдены{Color.RESET.value}')

            except KeyError as ex:
                ex_message = f'{Color.RED.value}Некорректный выбор пункта меню, попробуйте ещё раз{Color.RESET.value}'
                print(ex_message)

    def processing_add_book(self) -> None:
        print(f"{Color.MAGENTA.value}Добавление книги{Color.RESET.value}")
        print("Введите -1 для выхода в главное меню")
        print("Enter чтобы продолжить")

        while True:
            choice = input('-> ')

            if choice == '-1':
                return

            author = input('Введите автора -> ')
            title = input('Введите название -> ')
            year = input('Введите год -> ')

            result = self.check_year(year)

            if result != 'valid':
                print(result)
                print("Enter чтобы продолжить")
                continue
            else:
                year = int(year)

            try:
                self.writer.add_book(title, author, year)
                print(f'{Color.GREEN.value}Книга добавлена успешно{Color.RESET.value}')
            except FileNotFoundError as ex:
                print(f'{Color.RED.value}{str(ex)}{Color.RESET.value}')

    def processing_edit_status(self) -> None:
        print(f"{Color.MAGENTA.value}Изменение статуса книги{Color.RESET.value}")
        print("Введите -1 для выхода в главное меню")
        print("Enter чтобы продолжить")

        while True:
            choice = input('-> ')

            if choice == '-1':
                return

            book_id = input('Введите id книги -> ')
            try:
                book_id = int(book_id)
            except ValueError as ex:
                print(f"{Color.RED.value}Некорректный id книги, id книги - это цело число{Color.RESET.value}")

            print("Выберите статус")
            print("0 - выдана")
            print("1 - в наличии")

            choice = input('-> ')
            if choice != '1' and choice != '0':
                print(f"{Color.RED.value}Не верно выбранный статус{Color.RESET.value}")
                continue

            try:
                new_status = 'выдана' if choice == '0' else 'в наличии'
                self.writer.update_status_book(book_id, new_status)
            except FileNotFoundError as ex:
                print(f"{Color.RED.value}{str(ex)}{Color.RESET.value}")
            except BookNotFoundError as ex:
                print(f"{Color.RED.value}{str(ex)}{Color.RESET.value}")

    def processing_delete_book(self) -> None:
        print(f"{Color.MAGENTA.value}Удаление книги{Color.RESET.value}")

        while True:
            print("Для выхода в главное меню введите -1")
            print("Enter чтобы продолжить")

            choice = input('-> ')
            if choice == '-1':
                return

            book_id = input('Введите id книги -> ')

            try:
                book_id = int(book_id)
            except ValueError as ex:
                print(f"{Color.RED.value}Некорректный id книги, id книги - это цело число{Color.RESET.value}")

            try:
                self.writer.remove_book(book_id)
                print(f"{Color.GREEN.value}Книга успешно удалена{Color.RESET.value}")
            except FileNotFoundError as ex:
                print(f"{Color.RED.value}{str(ex)}{Color.RESET.value}")
            except BookNotFoundError as ex:
                print(f"{Color.RED.value}{str(ex)}{Color.RESET.value}")

    def run(self) -> None:
        print(f"{Color.GREEN.value}Добро пожаловать в бибиотеку{Color.RESET.value}\n")
        while True:
            print(self.get_main_menu())
            choice = input('-> ')

            if choice == '-1':
                break

            try:
                self.menu_point[choice]()
            except KeyError as ex:
                ex_message = f'{Color.RED.value}Некорректный выбор пункта меню, попробуйте ещё раз{Color.RESET.value}'
                print(ex_message)


if __name__ == '__main__':
    app = App()
    app.run()
