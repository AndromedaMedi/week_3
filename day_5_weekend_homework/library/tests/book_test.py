import unittest
from models.book import Book
from models import books

class TestBook(unittest.TestCase):

    def test_book_has_a_title(self):
        self.assertEqual("The Power of Now", books.book2.title)
    
    def test_book_has_author(self):
        self.assertEqual("Stephen Hawkin", books.book1.author)

    def test_book_has_genre(self):
        self.assertEqual("Autobiography", books.book1.genre)

    def test_get_book_count(self):
        self.assertEqual(3, len(books.books))

    def test_add_book(self):
        new_book = Book("Neverwhere", "Neil Gaiman", "Fantasy Novel", True)
        books.add_new_book(self, new_book)
        self.assertEqual(4, len(books.books))

    def test_remove_book(self):
        books.remove_book(self, books.book1)
        self.assertSetEqual(2, len(books.books))