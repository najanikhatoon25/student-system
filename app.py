from flask import Flask, render_template, request, redirect
import sqlite3
import os

app = Flask(__name__)

DB_PATH = os.path.join(os.path.abspath(os.path.dirname(__file__)), "students.sqlite3")

print("Database Path:", DB_PATH)


# ---------------- HOME ----------------

@app.route("/")
def home():
    return render_template("index.html")


# ---------------- ADD ----------------

@app.route("/add", methods=["GET", "POST"])
def add():

    if request.method == "POST":

        name = request.form["name"]
        email = request.form["email"]
        age = request.form["age"]
        gender = request.form["gender"]
        course = request.form["Course"]

        connection = sqlite3.connect(DB_PATH)
        cursor = connection.cursor()

        cursor.execute("""
        INSERT INTO students(name,email,age,gender,course)
        VALUES(?,?,?,?,?)
        """, (name, email, age, gender, course))

        connection.commit()
        connection.close()

        return redirect("/view")

    return render_template("add.html")


# ---------------- VIEW ----------------

@app.route("/view")
def view():

    connection = sqlite3.connect(DB_PATH)
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM students")

    students = cursor.fetchall()

    connection.close()

    return render_template("view_student.html", students=students)


# ---------------- SEARCH ----------------

@app.route("/search", methods=["GET", "POST"])
def search():

    student = None
    message = ""

    if request.method == "POST":

        student_id = request.form.get("student_id")

        connection = sqlite3.connect(DB_PATH)
        cursor = connection.cursor()

        cursor.execute(
            "SELECT * FROM students WHERE id=?",
            (student_id,)
        )

        student = cursor.fetchone()

        connection.close()

        if student is None:
            message = "❌ Student Not Found"

    return render_template(
        "search_student.html",
        student=student,
        message=message
    )

# ---------------- UPDATE ----------------

@app.route("/update", methods=["GET", "POST"])
def update():

    if request.method == "POST":

        student_id = request.form["id"]
        name = request.form["name"]
        email = request.form["email"]
        age = request.form["age"]
        gender = request.form["gender"]
        course = request.form["course"]

        connection = sqlite3.connect(DB_PATH)
        cursor = connection.cursor()

        cursor.execute("""
        UPDATE students
        SET
            name=?,
            email=?,
            age=?,
            gender=?,
            course=?
        WHERE id=?
        """, (name, email, age, gender, course, student_id))

        connection.commit()
        connection.close()

        return redirect("/view")

    return render_template("update_student.html")


# ---------------- DELETE ----------------

@app.route("/delete", methods=["GET", "POST"])
def delete():

    message = ""

    if request.method == "POST":

        student_id = request.form["student_id"]

        connection = sqlite3.connect(DB_PATH)
        cursor = connection.cursor()

        cursor.execute(
            "SELECT * FROM students WHERE id=?",
            (student_id,)
        )

        student = cursor.fetchone()

        if student:

            cursor.execute(
                "DELETE FROM students WHERE id=?",
                (student_id,)
            )

            connection.commit()

            message = "Student Deleted Successfully"

        else:

            message = "Student ID Not Found"

        connection.close()

    return render_template(
        "delete.html",
        message=message
    )


# ---------------- RUN ----------------

if __name__ == "__main__":
    app.run(debug=True)