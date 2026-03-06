from flask import Flask, render_template, request
import sqlite3
import os

app = Flask(__name__)

def init_db():
    conn = sqlite3.connect("students.db")
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS students(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            sapid TEXT,
            age INTEGER,
            marks INTEGER
        )
    ''')
    conn.commit()
    conn.close()

init_db()

@app.route("/")
def index():
    conn = sqlite3.connect("students.db")
    c = conn.cursor()
    c.execute("SELECT * FROM students")
    users = c.fetchall()
    conn.close()
    return render_template("index.html", users=users)

@app.route("/submit", methods=["POST"])
def submit():
    name = request.form["name"]
    sapid = request.form["sapid"]
    age = request.form["age"]
    marks = request.form["marks"]

    conn = sqlite3.connect("students.db")
    c = conn.cursor()
    c.execute(
        "INSERT INTO students (name, sapid, age, marks) VALUES (?, ?, ?, ?)",
        (name, sapid, age, marks)
    )
    conn.commit()
    conn.close()

    return "Student Added Successfully!"

@app.route("/search", methods=["POST"])
def search():
    name = request.form["search_name"]

    conn = sqlite3.connect("students.db")
    c = conn.cursor()
    c.execute("SELECT * FROM students WHERE name LIKE ?", ('%' + name + '%',))
    result = c.fetchall()
    conn.close()

    return render_template("index.html", users=result)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
