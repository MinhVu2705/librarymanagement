import sqlite3
import tkinter as tk
from tkinter import ttk, messagebox

# Database setup
def init_db():
    conn = sqlite3.connect("library.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS books (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            author TEXT NOT NULL,
            year INTEGER NOT NULL
        )
    """)
    conn.commit()
    conn.close()

# Add book to database
def add_book():
    title = entry_title.get()
    author = entry_author.get()
    year = entry_year.get()
    
    if not title or not author or not year:
        messagebox.showerror("Error", "All fields are required!")
        return
    
    conn = sqlite3.connect("library.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO books (title, author, year) VALUES (?, ?, ?)", (title, author, year))
    conn.commit()
    conn.close()
    load_books()
    entry_title.delete(0, tk.END)
    entry_author.delete(0, tk.END)
    entry_year.delete(0, tk.END)

# Load books from database
def load_books(search_query=None):
    for row in tree.get_children():
        tree.delete(row)
    
    conn = sqlite3.connect("library.db")
    cursor = conn.cursor()
    if search_query:
        cursor.execute("SELECT * FROM books WHERE title LIKE ? OR author LIKE ?", (f"%{search_query}%", f"%{search_query}%"))
    else:
        cursor.execute("SELECT * FROM books")
    rows = cursor.fetchall()
    conn.close()
    
    for row in rows:
        tree.insert("", tk.END, values=row)

# Delete selected book
def delete_book():
    selected_item = tree.selection()
    if not selected_item:
        messagebox.showerror("Error", "No book selected!")
        return
    
    book_id = tree.item(selected_item)['values'][0]
    conn = sqlite3.connect("library.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM books WHERE id = ?", (book_id,))
    conn.commit()
    conn.close()
    load_books()

# Search function
def search_book():
    search_query = entry_search.get()
    load_books(search_query)

# GUI Setup
root = tk.Tk()
root.title("Library Management")
root.geometry("600x550")
root.configure(bg="#f0f0f0")

frame = tk.Frame(root, bg="#ffffff", padx=10, pady=10, bd=2, relief=tk.RIDGE)
frame.pack(pady=10, padx=10, fill=tk.X)

# Labels and Entry Fields
tk.Label(frame, text="Title", bg="#ffffff", font=("Arial", 12)).grid(row=0, column=0, padx=5, pady=5)
tk.Label(frame, text="Author", bg="#ffffff", font=("Arial", 12)).grid(row=1, column=0, padx=5, pady=5)
tk.Label(frame, text="Year", bg="#ffffff", font=("Arial", 12)).grid(row=2, column=0, padx=5, pady=5)

entry_title = tk.Entry(frame, font=("Arial", 12))
entry_author = tk.Entry(frame, font=("Arial", 12))
entry_year = tk.Entry(frame, font=("Arial", 12))

entry_title.grid(row=0, column=1, padx=5, pady=5)
entry_author.grid(row=1, column=1, padx=5, pady=5)
entry_year.grid(row=2, column=1, padx=5, pady=5)

# Buttons
tk.Button(frame, text="Add Book", command=add_book, bg="#4CAF50", fg="white", font=("Arial", 12), padx=5, pady=5).grid(row=3, column=0, columnspan=2, pady=5, sticky="ew")
tk.Button(frame, text="Delete Book", command=delete_book, bg="#f44336", fg="white", font=("Arial", 12), padx=5, pady=5).grid(row=4, column=0, columnspan=2, pady=5, sticky="ew")

# Search Field
search_frame = tk.Frame(root, bg="#ffffff", padx=10, pady=5, bd=2, relief=tk.RIDGE)
search_frame.pack(pady=5, padx=10, fill=tk.X)

tk.Label(search_frame, text="Search", bg="#ffffff", font=("Arial", 12)).grid(row=0, column=0, padx=5, pady=5)
entry_search = tk.Entry(search_frame, font=("Arial", 12))
entry_search.grid(row=0, column=1, padx=5, pady=5)
tk.Button(search_frame, text="Search", command=search_book, bg="#2196F3", fg="white", font=("Arial", 12), padx=5, pady=5).grid(row=0, column=2, padx=5, pady=5)

# Book List Display
tree_frame = tk.Frame(root, bg="#ffffff", padx=10, pady=10, bd=2, relief=tk.RIDGE)
tree_frame.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

tree = ttk.Treeview(tree_frame, columns=("ID", "Title", "Author", "Year"), show="headings")
tree.heading("ID", text="ID")
tree.heading("Title", text="Title")
tree.heading("Author", text="Author")
tree.heading("Year", text="Year")

tree.column("ID", width=50, anchor=tk.CENTER)
tree.column("Title", width=200, anchor=tk.W)
tree.column("Author", width=150, anchor=tk.W)
tree.column("Year", width=80, anchor=tk.CENTER)

style = ttk.Style()
style.configure("Treeview", font=("Arial", 12), rowheight=25)
style.configure("Treeview.Heading", font=("Arial", 14, "bold"))

tree.pack(fill=tk.BOTH, expand=True)

# Initialize and Load Data
init_db()
load_books()

root.mainloop()
