from flask import Flask, render_template, request, flash, g, abort
import os
import sqlite3
from fdatabase import FDataBase

DATABASE = 'courses.db'
DEBUG = True
SECRET_KEY = '76b50cbbaf879cb4e7d492009e6bb1537f2453e1'

app = Flask(__name__)
app.config.from_object(__name__)
app.config.update(DATABASE=os.path.join(app.root_path, 'courses.db'))


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
    return render_template('index.html', menu=dbase.get_menu(), courses=dbase.get_courses_annonce())


@app.route("/add_courses", methods=["POST", "GET"])
def add_courses():
    db = get_db()
    dbase = FDataBase(db)

    if request.method == "POST":
        if len(request.form['name']) > 4 and len(request.form['courses']) > 10:
            res = dbase.add_courses(request.form['name'], request.form['price'], request.form['courses'],
                                    request.form['url'])
            if not res:
                flash("Ошибка добавления статьи", category="error")
            else:
                flash("Статья добавлена успешно", category="success")
        else:
            flash("Ошибка добавления статьи", category="error")

    return render_template('add_courses.html', title="Добавление курса",  menu=dbase.get_menu())


@app.route("/cours/<alias>")
def show_courses(alias):
    db = get_db()
    dbase = FDataBase(db)
    title, price, cours = dbase.get_courses(alias)
    if not title:
        abort(404)
    return render_template('cours.html', menu=dbase.get_menu(), title=title, price=price, cours=cours)


@app.errorhandler(404)
def page_not_found(error):
    db = get_db()
    dbase = FDataBase(db)
    return render_template('page404.html', title="Страница не найдена", menu=dbase.get_menu())


@app.teardown_appcontext
def close_db(error):
    if hasattr(g, 'link_db'):
        g.link_db.close()


if __name__ == '__main__':
    app.run()
