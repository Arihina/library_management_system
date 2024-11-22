from app.models.book import Book

# from models.book import Book


class MemoryLibrary:
    """
    Class for saving books in memory (dict)
    """
    def __init__(self):
        self.__library: dict[int, Book] = dict()

    @property
    def library(self) -> dict[int, Book]:
        return self.__library
