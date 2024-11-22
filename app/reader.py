# from app.storage import MemoryLibrary
# from app.models.book import Book


from models.book import Book
from storage import MemoryLibrary


class MemoryReader:
    """
    Class for get and search books in RAM memory (dict)
    """

    def __init__(self, library: MemoryLibrary):
        """
        :param library: (MemoryLibrary) The main memory storage for books
        """
        self.__library = library.library

    def get_all_books(self) -> list[Book]:
        """
        Get all books from storage
        :return: List of books
        """
        pass

    def get_part_books(self, limit: int = 10) -> list[Book]:
        """
        Get limit counts of books from storage
        :param limit: The number of books received (default is 10)
        :return: List of books with a length limit
        """
        pass

    def search_books_by_title(self, title: str, limit: int = 10) -> list[Book]:
        """
        Get filtered books by title
        :param title: Filter parameter
        :param limit:  The number of books received (default is 10)
        :return: List of filtered books by title
        """

    def search_books_by_author(self, author: str, limit: int = 10) -> list[Book]:
        """
        Get filtered books by author
        :param author: Filter parameter
        :param limit: The number of books received (default is 10)
        :return: List of filtered books by author
        """

    def search_books_by_year(self, year: int, limit: int = 10) -> list[Book]:
        """
        Get filtered books by year
        :param year: Filter parameter
        :param limit: The number of books received (default is 10)
        :return: List of filtered books by year
        """
