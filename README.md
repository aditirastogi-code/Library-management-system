# Library Management System

## Overview

The Library Management System is a menu-driven, console-based Python application that automates the everyday work of a small library. A librarian can add books and check their status (protected by an authorization number), while students can issue books, return them, and join a waiting list when a book is unavailable. The system also calculates a late-return fine automatically.

## Features

- **Add books (librarian only):** store book name, ID, author, category and number of copies.
- **Check book status (librarian only):** view every book with its details, available copies, current borrowers and waiting list.
- **Authorization check:** librarian actions are protected by an authorization number, with a limited number of attempts.
- **Issue a book:** students borrow a book using their registration number; available copies decrease automatically.
- **Waiting list:** if all copies are issued, a student can join the waiting list and see their position.
- **Return a book:** validates that the student actually borrowed the book, then restores the copy count.
- **Late fine calculation:** a fine is charged when a book is kept for more than 7 days.
- **Case-insensitive search:** book names and registration numbers are matched regardless of capitalization.

## Technologies / Tools Used

- **Language:** Python 3.8+
- **Concepts:** functions, modules, lists, dictionaries, loops, conditionals, user input handling
- **Standard library only:** no external packages required
- **Editor/IDE:** any (VS Code, PyCharm, IDLE, etc.)

## Project Structure

```
library-management/
├── main.py            # Entry point: menu and command handling
├── Librarian.py       # authorization(), enter_the_name_of_books(), check_status()
├── Student_acess.py   # issue_a_book(), return_a_book()
├── README.md
└── statement.md
```

> Rename `main.py` to whatever your main script file is called.

## Steps to Install & Run

1. **Install Python 3.8 or later** from [python.org](https://www.python.org/downloads/) and confirm it works:
   ```bash
   python --version
   ```
2. **Get the project files** (clone or download) and place `main.py`, `Librarian.py` and `Student_acess.py` in the **same folder**:
   ```bash
   git clone <your-repository-url>
   cd library-management
   ```
3. **Run the program:**
   ```bash
   python main.py
   ```
4. **Use the menu:**

   | Command | Action |
   |---------|--------|
   | 1 | Add a book (requires authorization number) |
   | 2 | Check book status (requires authorization number) |
   | 3 | Issue a book |
   | 4 | Return a book |
   | 5 | Exit |

   The authorization number is displayed when the program starts: `8624357`.

## Instructions for Testing

The project is tested manually through the console. Run `python main.py` and follow these scenarios.

| # | Scenario | Steps | Expected result |
|---|----------|-------|-----------------|
| 1 | Correct authorization | Command `1`, enter `8624357` | Prompts for book details |
| 2 | Wrong authorization | Command `1`, enter a wrong number repeatedly | "Access denied" with remaining attempts, then "Trial limit reached" |
| 3 | Add a book | Add "Python Basics", ID `B1`, 2 copies | Book is stored |
| 4 | Check status | Command `2` | All book details are listed |
| 5 | Issue an available book | Command `3`, book "Python Basics", reg no `21bcs001` | "The book is available"; copies drop from 2 to 1 |
| 6 | Issue an unavailable book | Issue all copies, then request again | "The book is not available"; answering `yes` adds you to the waiting list with your position |
| 7 | Book not in library | Command `3` with an unknown title | "There is no such book in our library" |
| 8 | Return on time | Command `4`, valid reg no, days = `7` | Copy returned, no fine |
| 9 | Return late | Command `4`, valid reg no, days = `8` | Fine of 250 |
| 10 | Return late (longer) | days = `15` | Fine of 260 (250 + 10 per extra week) |
| 11 | Return by wrong student | Command `4` with a reg no that never borrowed the book | "No record of this student borrowing this book." |
| 12 | Invalid menu input | Enter `9` | "Invalid command" |

**Fine formula used:** `250 + ((days - 8) // 7) * 10` for `days > 7`.

## Screenshots

_Add screenshots of the program running here (optional but recommended):_

```
![Main menu](screenshots/menu.png)
![Adding a book](screenshots/add_book.png)
![Issuing a book](screenshots/issue_book.png)
![Fine calculation](screenshots/fine.png)
```

## Author

Your Name – Your Registration Number / Course