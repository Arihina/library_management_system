import json
import os

from tools.exceptions.book_exc import BookNotFoundError
from tools.models.book import Book


class FileWriter:
    """
    Class for working with books in json file
    """

    def __init__(self):
        self.file_path = os.path.join(os.path.dirname(__file__), '../../resources/library.json')

    def add_book(self, title: str, author: str, year: int) -> None:
        """
        Add Book in library (json)
        :param title: (str) The title of the book
        :param author: (str) The author of the book
        :param year: (int) The year of the book's release
        """

        try:
            with open(self.file_path, 'r', encoding='utf-8') as file:
                books = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            raise FileNotFoundError('Не найден файл library.json в папке resources')

        book = Book(title, author, year)
        book = book.to_dict()
        books.append(book)

        with open(self.file_path, 'w', encoding='utf-8') as file:
            json.dump(books, file, ensure_ascii=False, indent=4)

    def remove_book(self, book_id: int) -> None:
        """
        Remove Book from library (json)
        :param book_id: (int) The id of the book
        """

        try:
            with open(self.file_path, 'r', encoding='utf-8') as file:
                books = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            raise FileNotFoundError('Не найден файл library.json в папке resources')

        f = False
        for book in books:
            if book['id'] == book_id:
                books.remove(book)
                f = True
                break

        if f is False:
            raise BookNotFoundError(f'Не найдена книга с id {book_id}')

        with open(self.file_path, 'w', encoding='utf-8') as file:
            json.dump(books, file, ensure_ascii=False, indent=4)

    def update_status_book(self, book_id: int, status: str) -> None:
        """
        Update status of Book
        :param book_id: (int) The id of the book
        :param status: (str) New status for book
        """

        if status != 'в наличии' and status != 'выдана':
            raise ValueError('Статус книги может быть только в наличии / выдана')

        try:
            with open(self.file_path, 'r', encoding='utf-8') as file:
                books = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            raise FileNotFoundError('Не найден файл library.json в папке resources')

        f = False
        for book in books:
            if book['id'] == book_id:
                if book['status'] == 'в наличии':
                    book['status'] = 'выдана'
                else:
                    book['status'] = 'в наличии'

                f = True
                break

        if f is False:
            raise BookNotFoundError(f'Не найдена книга с id {book_id}')

        with open(self.file_path, 'w', encoding='utf-8') as file:
            json.dump(books, file, ensure_ascii=False, indent=4)
