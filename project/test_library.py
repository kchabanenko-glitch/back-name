import pytest
from book_library import Book, Library
from typing import List


# ==============================================================================
# ФІКСТУРИ (FIXTURES)
# Фікстури створюють необхідні об'єкти для тестів, запобігаючи дублюванню коду.
# ==============================================================================

@pytest.fixture
def sample_books() -> List[Book]:
    """Фікстура, що повертає список тестових об'єктів Book."""
    print("\n-- Створення фікстури: sample_books --")
    return [
        Book(author="Автор 1", title="Книга A"),
        Book(author="Автор 2", title="Книга B"),
        Book(author="Автор 3", title="Книга C")
    ]


@pytest.fixture
def empty_library() -> Library:
    """Фікстура, що повертає порожній об'єкт Library."""
    print("\n-- Створення фікстури: empty_library --")
    return Library(name="Тестова Бібліотека")


@pytest.fixture
def populated_library(empty_library: Library, sample_books: List[Book]) -> Library:
    """Фікстура, що повертає об'єкт Library з попередньо доданими книгами."""
    print("\n-- Створення фікстури: populated_library --")
    for book in sample_books:
        empty_library.books.append(book)
    return empty_library




class TestBook:

    @pytest.mark.parametrize("author, title", [
        ("Леся Українка", "Лісова пісня"),
        ("Іван Франко", "Захар Беркут"),
    ])
    def test_book_initialization(self, author: str, title: str):
        book = Book(author, title)
        assert book.author == author
        assert book.title == title
        assert isinstance(book.id, str)
        assert len(book.id) > 10

    def test_book_id_is_unique(self):
        book1 = Book("А1", "Т1")
        book2 = Book("А2", "Т2")
        assert book1.id != book2.id


class TestLibrary:

    def test_library_initialization(self, empty_library: Library):
        assert empty_library.name == "Тестова Бібліотека"
        assert isinstance(empty_library.books, list)
        assert len(empty_library.books) == 0

    def test_add_book(self, empty_library: Library, sample_books: List[Book]):
        book_to_add = sample_books[0]
        empty_library.add_book(book_to_add)

        assert len(empty_library.books) == 1
        assert empty_library.books[0] is book_to_add

    def test_remove_book_success(self, populated_library: Library, sample_books: List[Book]):
        book_to_remove = sample_books[1]
        initial_count = len(populated_library.books)


        was_removed = populated_library.remove_book(book_to_remove.id)


        assert was_removed is True
        assert len(populated_library.books) == initial_count - 1

        assert book_to_remove not in populated_library.books

    def test_remove_book_not_found(self, populated_library: Library):
        non_existent_id = "неіснуючий-id-123"
        initial_count = len(populated_library.books)


        was_removed = populated_library.remove_book(non_existent_id)

        assert was_removed is False
        assert len(populated_library.books) == initial_count
