import os.path

from flask import Flask, render_template, request, flash, g
import sqlite3
from fdatabase import FDataBase

DATABASE = 'flsk.db'
DEBUG = True
SECRET_KEY = '5ee79c9338b7d91b165322247f1ba71907f7cb7f'

app = Flask(__name__)
app.config.from_object(__name__)
app.config.update(DATABASE = os.path.join(app.root_path, 'flsk.db'))


def connect_db():
    con = sqlite3.connect(app.config['DATABASE'])
    con.row_factory = sqlite3.Row
    return con


def create_db():
    db = connect_db()
    with app.open_resource('sq_db.sql', mode='r') as f:
        db.cursor().executescript(f.read())
    db.commit()
    db.close()


def get_db():
    if not hasattr(g, 'link_db'):
        g.link_db = connect_db()
    return g.link_db


@app.route("/")
def index():
    db = get_db()
    dbase = FDataBase(db)
    return render_template('index.html', title="Главная", menu=dbase.get_menu())


@app.route("/add_post", methods=["POST", "GET"])
def add_post():
    db = get_db()
    dbase = FDataBase(db)
    return render_template('add_post.html', title="Добавление страницы", menu=dbase.get_menu())


@app.errorhandler(404)
def page_not_found(error):
    db = get_db()
    dbase = FDataBase(db)
    return render_template('page404.html', title="Страница не найдена", menu=dbase.get_menu())


@app.teardown_appcontext
def close_db(error):
    if not hasattr(g, 'link_db'):
        g.link_db.close()


if __name__ == '__main__':
    app.run()
