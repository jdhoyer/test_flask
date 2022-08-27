# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

from flask import Flask, render_template, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app_flask = Flask(__name__)
app_flask.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app_flask)


class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=False)
    completed = db.Column(db.Integer, default=0)
    date_create = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return 'Task %r' % self.id

@app_flask.route('/')
def index():
    return render_template('index.html')


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    app_flask.run(debug=True)


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
