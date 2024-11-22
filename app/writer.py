from models.book import Book


class MemoryWriter:
    """
    Class for working with books in RAM memory (dict)
    """

    def __init__(self):
        self.__library: dict[int, Book] = dict()

    @property
    def library(self) -> dict[int, Book]:
        return self.__library

    def add_book(self, title: str, author: str, year: int) -> None:
        """
        Add Book in library (dict)
        :param title: (str) The title of the book
        :param author: (str) The author of the book
        :param year: (int) The year of the book's release
        """

        if year <= 0:
            raise ValueError('Год должен быть больше чем 0')
        if not author:
            raise ValueError('Длина имени автора должна быть больше чем 0')
        if not title:
            raise ValueError('Длина названия должна быть больше чем 0')

        book = Book(title, author, year)
        self.__library[book.id] = book

    def remove_book(self, book_id: int) -> None:
        """
        Remove Book from library (dict)
        :param book_id: (int) The id of the book
        """

        if book_id in self.__library:
            self.__library.pop(book_id)
        else:
            raise KeyError(f"Книга с id {book_id} не найдена в библиотеке")

    def update_status_book(self, book_id: int, status: str) -> None:
        """
        Update status of Book
        :param book_id: (int) The id of the book
        :param status: (str) New status for book
        """

        if status != 'в наличии' and status != 'выдана':
            raise ValueError('Статус книги может быть только в наличии / выдана')

        if self.__library[book_id]:
            self.__library[book_id].change_status()
        else:
            raise KeyError(f"Книга с id {book_id} не найдена в библиотеке")
