import os
import sqlite3

print('cwd:', os.getcwd())
print('file dir:', os.path.abspath(os.path.dirname(__file__)))
DB_PATH = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'students.db')
print('DB_PATH:', DB_PATH)

try:
    conn = sqlite3.connect(DB_PATH)
    conn.execute('CREATE TABLE IF NOT EXISTS test (id INTEGER PRIMARY KEY)')
    conn.commit()
    conn.close()
    print('Connected and created table OK')
except Exception as e:
    print('ERROR:', type(e), e)
