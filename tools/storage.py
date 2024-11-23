from tools.models.book import Book


class MemoryLibrary:
    """
    Class for saving books in memory (dict)
    """

    def __init__(self):
        self.__library: dict[int, Book] = dict()

    @property
    def library(self) -> dict[int, Book]:
        return self.__library

    def load_books_from_dict(self, books: dict[int, Book]) -> None:
        """
        Load books from prepare dict
        :param books: (dict[int, Book]) Dict with books
        """
        self.__library = books
