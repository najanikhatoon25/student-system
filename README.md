# Student Management (Flask)

Simple Flask app to manage student records using SQLite.

## Project Structure

- app.py — Flask application with routes for add, view, search, update, delete.
- students.sqlite3 — SQLite database file (pre-included).
- templates/ — HTML templates for the UI.
- static/style.css — basic styles.

## Requirements

- Python 3.8+
- Flask

Install dependencies:

```bash
python3 -m pip install Flask
```

## Run

Start the app:

```bash
python3 app.py
```

Open http://127.0.0.1:5000 in your browser.

## Notes

- Database path is `students.sqlite3` in the project root.
- Routes: `/` (home), `/add`, `/view`, `/search`, `/update`, `/delete`.

Feel free to ask me to expand this README with usage examples or screenshots.
