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
            '2': self.get_sub_find_menu,
            '3': self.get_sub_add_menu,
            '4': self.get_sub_edit_menu,
            '5': self.get_sub_delete_menu
        }

    def get_main_menu(self) -> str:
        return (f"Главное меню\n"
                f"(1) Просмотреть все книги\n"
                f"(2) Найти книгу\n"
                f"(3) Добавить книгу\n"
                f"(4) Изменить статус книги\n"
                f"(5) Удалить книгу\n"
                f"(0) {Color.RED.value}Выход{Color.RESET.value}")

    def show_all_books(self):
        try:
            books = self.reader.get_all()
        except FileNotFoundError as ex:
            print(f'{Color.RED.value}{str(ex)}{Color.RESET.value}')
            return

        print(f'{Color.BLUE.value}Все книги{Color.RESET.value}')

        for book in books:
            print(book)
        print()

    def get_sub_find_menu(self) -> str:
        pass

    def get_sub_add_menu(self) -> str:
        pass

    def get_sub_edit_menu(self) -> str:
        pass

    def get_sub_delete_menu(self) -> str:
        pass

    def run(self) -> None:
        print(f"{Color.GREEN.value}Добро пожаловать в бибиотеку{Color.RESET.value}\n")
        while True:
            print(self.get_main_menu())
            choice = input('-> ')

            if choice == '0':
                break

            try:
                self.menu_point[choice]()
            except KeyError as ex:
                ex_message = f'{Color.RED.value}Некорректный выбор пункта меню, попробуйте ещё раз{Color.RESET.value}'
                print(ex_message)


if __name__ == '__main__':
    app = App()
    app.run()
