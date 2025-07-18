import math
import time
import sqlite3
import re
from flask import url_for


class FDataBase:
    def __init__(self, db):
        self.__db = db
        self.__cur = db.cursor()

    def get_menu(self):
        sql = "SELECT * FROM mainmenu"
        try:
            self.__cur.execute(sql)
            res = self.__cur.fetchall()
            if res:
                return res
        except IOError:
            print("Ошибка чтения из БД")
        return []

    def add_courses(self, title, price, text, url):
        try:
            self.__cur.execute("SELECT COUNT() as `count` FROM courses WHERE url LIKE ?", (url,))
            res = self.__cur.fetchone()
            if res['count'] > 0:
                print("Статья с таким url уже существует")
                return False

            tm = math.floor(time.time())
            self.__cur.execute("INSERT INTO courses VALUES(NULL, ?, ?, ?, ?, ?)", (title, price, text, url, tm))
            self.__db.commit()
        except sqlite3.Error as e:
            print("Ошибка добавления статьи в БД " + str(e))
            return False
        return True

    def get_courses(self, alias):
        try:
            self.__cur.execute(f"SELECT title, price, text FROM courses WHERE url = '{alias}'")
            res = self.__cur.fetchone()
            if res:
                return res
        except sqlite3.Error as e:
            print("Ошибка получения статьи из БД " + str(e))

        return False, False

    def get_courses_annonce(self):
        try:
            self.__cur.execute("SELECT id, title, price, text, url FROM courses ORDER BY time DESC")
            res = self.__cur.fetchall()
            if res:
                return res
        except sqlite3.Error as e:
            print("Ошибка получения статьи из БД " + str(e))

        return []
