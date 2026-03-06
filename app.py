from flask import Flask, render_template, request

app = Flask(__name__)

users = []

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    sapid = request.form['sapid']
    age = request.form['age']
    marks = request.form['marks']

    users.append({
        "name": name,
        "sapid": sapid,
        "age": age,
        "marks": marks
    })

    return render_template("index.html", users=users)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)