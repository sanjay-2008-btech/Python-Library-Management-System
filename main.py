"""
Library Management System
A beginner-friendly Python project demonstrating OOP concepts.
Run: python main.py
"""

from abc import ABC, abstractmethod


class Book:
    """Represents a book in the library."""

    def __init__(self, title: str, author: str, book_id: int):
        self.title = title
        self.author = author
        self.book_id = book_id
        self.__is_available = True  # Encapsulation

    @property
    def is_available(self):
        return self.__is_available

    def borrow(self):
        if not self.__is_available:
            return False
        self.__is_available = False
        return True

    def return_book(self):
        if self.__is_available:
            return False
        self.__is_available = True
        return True

    def __str__(self):
        status = "Available" if self.__is_available else "Borrowed"
        return f"[{self.book_id}] {self.title} by {self.author} - {status}"


class Member(ABC):
    """Abstract base class for library members."""

    def __init__(self, name: str, member_id: int):
        self.name = name
        self.member_id = member_id
        self._borrowed_books = []

    @property
    @abstractmethod
    def borrowing_limit(self):
        """Return the maximum number of books this member can borrow."""
        raise NotImplementedError

    def borrow_book(self, book: Book):
        if len(self._borrowed_books) >= self.borrowing_limit:
            return False, "Borrowing limit reached."
        if not book.borrow():
            return False, "This book is already borrowed."
        self._borrowed_books.append(book)
        return True, f'"{book.title}" borrowed successfully.'

    def return_book(self, book_id: int):
        for book in self._borrowed_books:
            if book.book_id == book_id:
                book.return_book()
                self._borrowed_books.remove(book)
                return True, f'"{book.title}" returned successfully.'
        return False, "You have not borrowed a book with that ID."

    def list_borrowed_books(self):
        return list(self._borrowed_books)


class RegularMember(Member):
    """Regular members can borrow up to 2 books."""

    @property
    def borrowing_limit(self):
        return 2


class PremiumMember(Member):
    """Premium members can borrow up to 5 books."""

    @property
    def borrowing_limit(self):
        return 5


class Library:
    """Coordinates books and members."""

    def __init__(self):
        self.books = {}
        self.members = {}

    def add_book(self, book: Book):
        if book.book_id in self.books:
            return False
        self.books[book.book_id] = book
        return True

    def register_member(self, member: Member):
        if member.member_id in self.members:
            return False
        self.members[member.member_id] = member
        return True

    def show_books(self):
        if not self.books:
            print("No books in the library.")
        for book in self.books.values():
            print(book)

    def show_members(self):
        if not self.members:
            print("No registered members.")
        for member in self.members.values():
            print(
                f"ID: {member.member_id} | Name: {member.name} | "
                f"Type: {member.__class__.__name__} | "
                f"Borrowed: {len(member.list_borrowed_books())}/{member.borrowing_limit}"
            )


def create_sample_library():
    library = Library()
    sample_books = [
        Book("Python Crash Course", "Eric Matthes", 101),
        Book("Clean Code", "Robert C. Martin", 102),
        Book("The Alchemist", "Paulo Coelho", 103),
        Book("Atomic Habits", "James Clear", 104),
    ]
    for book in sample_books:
        library.add_book(book)

    library.register_member(RegularMember("Ananya", 1))
    library.register_member(PremiumMember("Rahul", 2))
    return library


def main():
    library = create_sample_library()

    while True:
        print("\n===== LIBRARY MANAGEMENT SYSTEM =====")
        print("1. View all books")
        print("2. View all members")
        print("3. Borrow a book")
        print("4. Return a book")
        print("5. View a member's borrowed books")
        print("6. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            library.show_books()

        elif choice == "2":
            library.show_members()

        elif choice == "3":
            try:
                member_id = int(input("Enter member ID: "))
                book_id = int(input("Enter book ID: "))
                member = library.members.get(member_id)
                book = library.books.get(book_id)
                if member is None:
                    print("Member not found.")
                elif book is None:
                    print("Book not found.")
                else:
                    success, message = member.borrow_book(book)
                    print(message)
            except ValueError:
                print("Please enter valid numeric IDs.")

        elif choice == "4":
            try:
                member_id = int(input("Enter member ID: "))
                book_id = int(input("Enter book ID: "))
                member = library.members.get(member_id)
                if member is None:
                    print("Member not found.")
                else:
                    success, message = member.return_book(book_id)
                    print(message)
            except ValueError:
                print("Please enter valid numeric IDs.")

        elif choice == "5":
            try:
                member_id = int(input("Enter member ID: "))
                member = library.members.get(member_id)
                if member is None:
                    print("Member not found.")
                else:
                    borrowed = member.list_borrowed_books()
                    if borrowed:
                        for book in borrowed:
                            print(book)
                    else:
                        print("This member has no borrowed books.")
            except ValueError:
                print("Please enter a valid numeric ID.")

        elif choice == "6":
            print("Thank you for using the Library Management System!")
            break

        else:
            print("Invalid choice. Please select 1-6.")


if __name__ == "__main__":
    main()
