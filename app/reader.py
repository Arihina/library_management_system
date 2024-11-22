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
        return [book for book in self.__library.values()]

    def get_part_books(self, limit: int = 10) -> list[Book]:
        """
        Get limit counts of books from storage
        :param limit: The number of books received (default is 10)
        :return: List of books with a length limit
        """
        if limit <= 0:
            raise ValueError('Количество книг для обработки должно быть больше чем 0')

        for i in range(0, len(self.__library), limit):
            yield self.__library.values()[i:i + limit]

    def search_books_by_title(self, title: str, limit: int = 10) -> list[Book]:
        """
        Get filtered books by title
        :param title: Filter parameter
        :param limit: The number of books taken for filtering at a time (default is 10)
        :return: List of filtered books by title
        """
        if limit <= 0:
            raise ValueError('Год должен быть больше чем 0')
        if len(title) == 0:
            raise ValueError('Длина названия должна быть больше чем 0')

        for i in range(0, len(self.__library), limit):
            unfiltered = self.__library.values()[i:i + limit]
            yield [book for book in unfiltered if book.title.lower() == title.lower()]

    def search_books_by_author(self, author: str, limit: int = 10) -> list[Book]:
        """
        Get filtered books by author
        :param author: Filter parameter
        :param limit: The number of books taken for filtering at a time (default is 10)
        :return: List of filtered books by author
        """
        if limit <= 0:
            raise ValueError('Количество книг для обработки должно быть больше чем 0')
        if len(author) == 0:
            raise ValueError('Длина имени автора должна быть больше чем 0')

        for i in range(0, len(self.__library), limit):
            unfiltered = self.__library.values()[i:i + limit]
            yield [book for book in unfiltered if book.author.lower() == author.lower()]

    def search_books_by_year(self, year: int, limit: int = 10) -> list[Book]:
        """
        Get filtered books by year
        :param year: Filter parameter
        :param limit: The number of books taken for filtering at a time (default is 10)
        :return: List of filtered books by year
        """
        if limit <= 0:
            raise ValueError('Количество книг для обработки должно быть больше чем 0')
        if year <= 0:
            raise ValueError('Год должен быть больше чем 0')

        for i in range(0, len(self.__library), limit):
            unfiltered = self.__library.values()[i:i + limit]
            yield [book for book in unfiltered if book.year == year]
