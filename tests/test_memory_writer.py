import unittest

from app.storage import MemoryLibrary
from app.writer.memory_writer import MemoryWriter


class TestMemoryWriter(unittest.TestCase):

    def setUp(self):
        self.lib = MemoryLibrary()
        self.writer = MemoryWriter(self.lib)

    def test_correct_add(self):
        self.writer.add_book('test title', 'test author', 1888)

        self.assertEqual(len(self.writer.library), 1)

        self.assertIn('test title', [book.title for book in self.writer.library.values()])
        self.assertIn('test author', [book.author for book in self.writer.library.values()])
        self.assertIn(1888, [book.year for book in self.writer.library.values()])

    def test_incorrect_add_year(self):
        with self.assertRaises(ValueError) as ex:
            self.writer.add_book('test title', 'test author', -1888)

        self.assertEqual(str(ex.exception), 'Год должен быть больше чем 0')

    def test_incorrect_add_title(self):
        with self.assertRaises(ValueError) as ex:
            self.writer.add_book('', 'test author', 1888)

        self.assertEqual(str(ex.exception), 'Длина названия должна быть больше чем 0')

    def test_incorrect_add_author(self):
        with self.assertRaises(ValueError) as ex:
            self.writer.add_book('test title', '', 1888)

        self.assertEqual(str(ex.exception), 'Длина имени автора должна быть больше чем 0')

    def test_correct_remove(self):
        self.writer.add_book('test title', 'test author', 1888)
        book_id = [book.id for book in self.writer.library.values()][0]

        self.writer.remove_book(book_id)
        self.assertEqual(len(self.writer.library), 0)

    def test_incorrect_remove(self):
        self.writer.add_book('test title', 'test author', 1888)

        with self.assertRaises(KeyError) as ex:
            self.writer.remove_book(-1)

        self.assertIsInstance(ex.exception, KeyError)

    def test_update_correct_status(self):
        self.writer.add_book('test title', 'test author', 1888)
        book_id = [book.id for book in self.writer.library.values()][0]

        self.writer.update_status_book(book_id, 'в наличии')

        self.writer.library[book_id].change_status()
        self.writer.update_status_book(book_id, 'выдана')

    def test_update_incorrect_status(self):
        self.writer.add_book('test title', 'test author', 1888)
        book_id = [book.id for book in self.writer.library.values()][0]

        with self.assertRaises(ValueError) as ex:
            self.writer.update_status_book(book_id, 'random status')

        self.assertEqual(str(ex.exception), 'Статус книги может быть только в наличии / выдана')

    def test_update_incorrect_id(self):
        self.writer.add_book('test title', 'test author', 1888)

        with self.assertRaises(KeyError) as ex:
            self.writer.remove_book(-1)

        self.assertIsInstance(ex.exception, KeyError)


if __name__ == '__main__':
    unittest.main()

