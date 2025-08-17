import mysql.connector

def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="Enter Password",
        database="library_db"
    )





    

# --- Books CRUD ---
def add_book(title, author, price, quantity):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO books (title, author, price, quantity) VALUES (%s, %s, %s, %s)",
        (title, author, price, quantity)
    )
    conn.commit()
    conn.close()

def view_books():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM books")
    rows = cursor.fetchall()
    conn.close()
    return rows

def update_book(book_id, price, quantity):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE books SET price=%s, quantity=%s WHERE id=%s",
        (price, quantity, book_id)
    )
    conn.commit()
    conn.close()

def delete_book(book_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM books WHERE id=%s", (book_id,))
    conn.commit()
    conn.close()

def search_books(keyword):
    conn = get_connection()
    cursor = conn.cursor()
    query = "SELECT * FROM books WHERE title LIKE %s OR author LIKE %s"
    like = f"%{keyword}%"
    cursor.execute(query, (like, like))
    rows = cursor.fetchall()
    conn.close()
    return rows

# --- Members CRUD ---
def add_member(name, email):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO members (name, email) VALUES (%s, %s)",
        (name, email)
    )
    conn.commit()
    conn.close()

def view_members():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM members")
    rows = cursor.fetchall()
    conn.close()
    return rows

def delete_member(member_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM members WHERE id=%s", (member_id,))
    conn.commit()
    conn.close()

def search_members(keyword):
    conn = get_connection()
    cursor = conn.cursor()
    query = "SELECT * FROM members WHERE name LIKE %s OR email LIKE %s"
    like = f"%{keyword}%"
    cursor.execute(query, (like, like))
    rows = cursor.fetchall()
    conn.close()
    return rows
