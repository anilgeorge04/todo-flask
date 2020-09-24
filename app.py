# TODO list flask app
from flask import Flask, redirect, render_template, request
# import sqlite3
from cs50 import SQL

app = Flask(__name__)

# create new to write on fresh each time
# open("todo.db", "w").close()

# start connection and setup cursor
# conn = sqlite3.connect("todo.db")
# set row factory property of connection object to sqlite3.Row to return list of dictionaries instead of tuples
# conn.row_factory = sqlite3.Row
# set cursor object
# db = conn.cursor()
db = SQL("sqlite:///todo.db")

@app.route('/', methods=["GET", "POST"])
def tasks():
    if request.method == "GET":
        todos = db.execute("SELECT * FROM todo")
        # convert sqlite3.Row objects to dictionary
        # todos = [dict(row) for row in db.fetchall()]
        return render_template('tasks.html', todos=todos)
    else:
        if request.form['submit'] == "Remove all":
            db.execute("DELETE FROM todo")
        elif request.form['submit'] == "Add Task":
            newtask = request.form.get("newtask")
            db.execute("INSERT INTO todo (task) VALUES (:task)", task=newtask)
        return redirect('/')


@app.route('/thankyou')
def thankyou():
    # Save and close
    # db.close()
    # conn.commit()
    # conn.close()
    return render_template('thankyou.html')
