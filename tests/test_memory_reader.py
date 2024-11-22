import unittest
from random import randint

from app.models.book import Book
from app.reader import MemoryReader
from app.storage import MemoryLibrary


class TestMemoryReader(unittest.TestCase):

    def setUp(self):
        def generate_books_dict(num_books: int) -> dict[int, Book]:
            books = {}

            for i in range(num_books):
                title = f"test title {randint(0, 3)}"
                author = f"test author {randint(0, 3)}"
                year = randint(2000, 2025)

                book = Book(title, author, year)
                books[book.id] = book

            return books

        self.test_dict = MemoryLibrary()
        self.test_dict.load_books_from_dict(generate_books_dict(15))
        self.test_books = [book for book in self.test_dict.library.values()]

        self.reader = MemoryReader(self.test_dict)

    def test_get_all_books(self):
        self.assertEqual(self.test_books, self.reader.get_all_books())

    def test_default_part_books(self):
        len_result = []
        for i in self.reader.get_part_books():
            len_result.append(len(i))

        len_answer = [10, 5]

        self.assertEqual(len_answer[0], len_result[0])
        self.assertEqual(len_answer[1], len_result[1])

    def test_incorrect_limit_search(self):
        with self.assertRaises(ValueError) as ex1:
            list(self.reader.search_books_by_author('test', -100))

        self.assertEqual(str(ex1.exception), 'Количество книг для обработки должно быть больше чем 0')

        with self.assertRaises(ValueError) as ex2:
            list(self.reader.search_books_by_title('test', -100))

        self.assertEqual(str(ex2.exception), 'Количество книг для обработки должно быть больше чем 0')

    def test_incorrect_params_search(self):
        with self.assertRaises(ValueError) as ex1:
            list(self.reader.search_books_by_author(''))

        self.assertEqual(str(ex1.exception), 'Длина имени автора должна быть больше чем 0')

        with self.assertRaises(ValueError) as ex2:
            list(self.reader.search_books_by_title(''))

        self.assertEqual(str(ex2.exception), 'Длина названия должна быть больше чем 0')
