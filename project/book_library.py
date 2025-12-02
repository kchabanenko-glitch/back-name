import uuid
from typing import List


class Book:

    def __init__(self, author: str, title: str):
        self.author: str = author
        self.title: str = title

        self.id: str = str(uuid.uuid4())

    def __str__(self) -> str:
        return f"'{self.title}' (Автор: {self.author}, ID: {self.id[:8]}...)"


class Library:


    def __init__(self, name: str):
        self.name: str = name
        self.books: List[Book] = []

    def add_book(self, book: Book) -> None:
        self.books.append(book)
        print(f"У бібліотеку '{self.name}' додано: {book.title}.")

    def remove_book(self, book_id: str) -> bool:
        initial_count = len(self.books)

        self.books = [book for book in self.books if book.id != book_id]

        if len(self.books) < initial_count:
            print(f"Книгу з ID {book_id[:8]}... успішно видалено з фондів.")
            return True
        else:
            print(f"Помилка: Книгу з ID {book_id[:8]}... не знайдено.")
            return False

    def display_books(self) -> None:
        print(f"\n--- Фонди бібліотеки '{self.name}' ({len(self.books)} книг) ---")
        if not self.books:
            print("Фонди порожні.")
            return

        for book in self.books:
            print(f"   {book}")
