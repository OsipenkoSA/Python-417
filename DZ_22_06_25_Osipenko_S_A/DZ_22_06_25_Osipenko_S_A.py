import sqlite3


with sqlite3.connect("education.db") as con:
    cur = con.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS student(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    surname TEXT NOT NULL,
    name TEXT NOT NULL,
    patronymic TEXT NOT NULL,
    age INTEGER NOT NULL CHECK(age >= 17 AND age <= 50),
    [group] TEXT NOT NULL,
    FOREIGN KEY ([group]) REFERENCES groups (id) ON DELETE RESTRICT
    )""")

    cur.execute("""CREATE TABLE IF NOT EXISTS groups(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        group_name  TEXT NOT NULL   
    )""")

    cur.execute("""CREATE TABLE IF NOT EXISTS lessons(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            lesson_title TEXT NOT NULL   
        )""")

    cur.execute("""CREATE TABLE IF NOT EXISTS association(
            lesson_id INTEGER,
            group_id INTEGER,
            PRIMARY KEY (lesson_id, group_id),
            FOREIGN KEY (lesson_id) REFERENCES lessons (id) ON DELETE RESTRICT,
            FOREIGN KEY (lesson_id) REFERENCES groups (id) ON DELETE RESTRICT
        )""")
