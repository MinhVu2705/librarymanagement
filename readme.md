Library Management System

Introduction

This is a simple Library Management System built using Python with a graphical user interface (GUI) implemented using tkinter and data storage using SQLite. The application allows users to:

Add books with title, author, and year.

View a list of books.

Search for books by title or author.

Delete selected books.

Installation

Requirements

Make sure you have Python installed on your system. The following dependencies are required:

- tkinter (built-in with Python)
- sqlite3 (built-in with Python)

Running the Application

Download or clone the project files.

Open a terminal or command prompt and navigate to the project folder.

Run the script using:

python library_management.py

Features

1. Add a Book

Enter the title, author, and year of the book in the input fields.

Click the "Add Book" button to save it to the database.

2. Search for a Book

Enter the title or author name in the search field.

Click the "Search" button to filter the book list.

3. Delete a Book

Select a book from the displayed list.

Click the "Delete Book" button to remove it.

Database Information

The application uses library.db as the database, which contains a table named books with the following fields:

id (INTEGER, Primary Key, Auto-increment)

title (TEXT, Not Null)

author (TEXT, Not Null)

year (INTEGER, Not Null)

Customization

You can modify the GUI layout and functionality by editing the library_management.py script. If you want to reset the database, delete library.db and restart the application.

License

This project is open-source and free to use for educational purposes.

