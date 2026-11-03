# Library Management System (Python OOP)

A simple command-line Library Management System built with Python. It demonstrates core Object-Oriented Programming concepts through a practical example.

## Features

- Display the books available in the library
- Register and display regular and premium members
- Borrow and return books
- View books borrowed by each member
- Prevent borrowing unavailable books and enforce borrowing limits

## OOP Concepts Demonstrated

| Concept | Implementation |
|---|---|
| Classes and Objects | `Book`, `Member`, `RegularMember`, `PremiumMember`, and `Library` |
| Encapsulation | `Book.__is_available` is private and accessed through a property and methods |
| Inheritance | `RegularMember` and `PremiumMember` inherit from `Member` |
| Polymorphism | Each member subclass provides its own `borrowing_limit` |
| Abstraction | `Member` is an abstract base class with an abstract `borrowing_limit` property |

## Requirements

- Python 3.8 or later
- No external packages required

## How to Run

1. Download or clone this repository.
2. Open a terminal in the project folder.
3. Run:

```bash
python main.py
```

On some systems, use `python3 main.py`.

## Sample Data

The program starts with four sample books and two members:

- Member ID `1`: Ananya (Regular member; limit: 2 books)
- Member ID `2`: Rahul (Premium member; limit: 5 books)

Use these IDs to try borrowing and returning books.

## Example

```text
===== LIBRARY MANAGEMENT SYSTEM =====
1. View all books
2. View all members
3. Borrow a book
4. Return a book
5. View a member's borrowed books
6. Exit
```

## Project Structure

```text
library_management_oop/
├── main.py
├── README.md
└── .gitignore
```

## Learning Objective

This project shows how Python OOP concepts can be used to model a real-world library. It is intended for educational use and can be extended with file storage, a database, a graphical interface, or fine calculations.

## Reference

The project idea is inspired by the educational Python OOP project examples shared here:
https://github.com/MostafaAhmed98/Python_OOP_Projects

This implementation is independently written for learning and demonstration.
