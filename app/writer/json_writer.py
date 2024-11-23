import json
import os

from app.models.book import Book


class FileWriter:
    """
    Class for working with books in json file
    """

    def __init__(self):
        self.current_directory = os.path.dirname(__file__)
        self.file_path = os.path.join(self.current_directory, '../../resources/library.json')

    def add_book(self, title: str, author: str, year: int) -> None:
        """
        Add Book in library (json)
        :param title: (str) The title of the book
        :param author: (str) The author of the book
        :param year: (int) The year of the book's release
        """

        book = Book(title, author, year)
        book = book.to_dict()

        with open(self.file_path, 'a', encoding='utf-8') as file:
            json.dump(book, file)
            file.write(',')

    def remove_book(self, book_id: int) -> None:
        """
        Remove Book from library (json)
        :param book_id: (int) The id of the book
        """
        pass

    def update_status_book(self, book_id: int, status: str) -> None:
        """
        Update status of Book
        :param book_id: (int) The id of the book
        :param status: (str) New status for book
        """
        pass
