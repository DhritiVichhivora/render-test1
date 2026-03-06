from flask import Flask, render_template, request
import sqlite3
import os

app = Flask(__name__)

# Connect to SQLite database
conn = sqlite3.connect("students.db", check_same_thread=False)
cursor = conn.cursor()

# Create table if it doesn't exist
cursor.execute("""
CREATE TABLE IF NOT EXISTS students(
    name TEXT,
    sapid TEXT,
    age INTEGER,
    marks INTEGER
)
""")
conn.commit()


# Home page
@app.route("/")
def index():
    cursor.execute("SELECT * FROM students")
    users = cursor.fetchall()
    return render_template("index.html", users=users)


# Form submission
@app.route("/submit", methods=["POST"])
def submit():

    name = request.form["name"]
    sapid = request.form["sapid"]
    age = request.form["age"]
    marks = request.form["marks"]

    cursor.execute(
        "INSERT INTO students VALUES (?,?,?,?)",
        (name, sapid, age, marks)
    )

    conn.commit()

    cursor.execute("SELECT * FROM students")
    users = cursor.fetchall()

    return render_template("index.html", users=users)


# Run the app (important for Render)
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
