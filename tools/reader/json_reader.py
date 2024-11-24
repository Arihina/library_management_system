import json
import os

from tools.models.book import Book
from tools.models.status import Status


class FileReader:
    """
        Class for get and search books in json file
        """

    def __init__(self):
        self.file_path = os.path.join(os.path.dirname(__file__), '../../resources/library.json')

    def get_all(self) -> list[Book]:
        """
        Get all books from storage
        :return: List of books
        """

        try:
            with open(self.file_path, 'r', encoding='utf-8') as file:
                books = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            raise FileNotFoundError('Не найден файл library.json в папке resources')

        result = []
        for book_data in books:
            book = Book(
                book_data['title'],
                book_data['author'],
                book_data['year'],
            )

            if book_data['status'] == 'выдана':
                book.status = Status.ISSUED
            else:
                book.status = Status.IN_STOCK

            book.id = book_data['id']

            result.append(book)

        return result

    def search_books_by_title(self, title: str) -> list[Book]:
        """
        Get filtered books by title
        :param title: Filter parameter
        :return: List of filtered books by title
        """

        if len(title) == 0:
            raise ValueError('Длина названия должна быть больше чем 0')

        books = self.get_all()
        return [book for book in books if book.title == title]

    def search_books_by_author(self, author: str) -> list[Book]:
        """
        Get filtered books by author
        :param author: Filter parameter
        :return: List of filtered books by author
        """

        if len(author) == 0:
            raise ValueError('Длина имени автора должна быть больше чем 0')

        books = self.get_all()
        return [book for book in books if book.author == author]

    def search_books_by_year(self, year: int) -> list[Book]:
        """
        Get filtered books by year
        :param year: Filter parameter
        :return: List of filtered books by year
        """

        if year <= 0:
            raise ValueError('Год должен быть больше чем 0')

        books = self.get_all()
        return [book for book in books if book.year == year]
