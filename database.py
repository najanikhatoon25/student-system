import sqlite3
import os

# Create database in project directory using absolute path
DB_PATH = os.path.join(os.path.abspath(os.path.dirname(__file__)), "students.sqlite3")

connection = sqlite3.connect(DB_PATH)

cursor = connection.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS students(

id INTEGER PRIMARY KEY AUTOINCREMENT,
name TEXT NOT NULL,
email TEXT NOT NULL,
age INTEGER,
gender TEXT,
course TEXT

)
""")

connection.commit()
connection.close()

print("Database Created")