# TODO list flask app
from flask import Flask, redirect, render_template, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todos.db'
db = SQLAlchemy(app)


class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=False)
    completed = db.Column(db.Integer, default=0)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<Task %r>' % self.id


@app.route('/', methods=['GET', 'POST'])
def tasks():
    if request.method == "GET":
        todos = Todo.query.order_by(Todo.completed, Todo.date_created).all()
        return render_template('tasks.html', todos=todos)
    else:
        if request.form['submit'] == "Remove all":
            try:
                db.session.query(Todo).delete()
                db.session.commit()
                return redirect('/')
            except:
                return "There was an issue deleting all tasks"

        elif request.form['submit'] == "Add Task":
            newtask = Todo(content=request.form.get("newtask"))
            try:
                db.session.add(newtask)
                db.session.commit()
                return redirect('/')
            except:
                return "There was an issue adding that task"


@app.route('/delete/<int:id>')
def delete(id):
    task_to_del = Todo.query.get_or_404(id)
    try:
        db.session.delete(task_to_del)
        db.session.commit()
        return redirect('/')
    except:
        return "There was an issue in deleting that task"


@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    task_to_upd = Todo.query.get_or_404(id)
    if request.method == 'POST':
        task_to_upd.content = request.form.get("updtask")
        try:
            db.session.commit()
            return redirect('/')
        except:
            return "There was an issue updating that task"
    else:
        return render_template('update.html', task=task_to_upd)


@app.route('/complete/<int:id>')
def complete(id):
    task_to_comp = Todo.query.get_or_404(id)
    task_to_comp.completed = 1
    try:
        db.session.commit()
        return redirect('/')
    except:
        return "There was an issue in marking that task as complete"

@app.route('/thankyou')
def thankyou():
    return render_template('thankyou.html')


if __name__ == "__main__":
    app.run(debug=True)
