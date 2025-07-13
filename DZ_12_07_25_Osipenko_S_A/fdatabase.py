import math
import time
import sqlite3


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

    def reserv(self, name, phone, room, people, days, date_reserv):
        try:
            tm = math.floor(time.time())
            self.__cur.execute("INSERT INTO reserv VALUES(NULL, ?, ?, ?, ?, ?, ?, ?)",
                               (name, phone, room, people, days, date_reserv, tm))
            self.__cur.commit()
            return True
        except sqlite3.Error as e:
            print("Ошибка добавления брони в БД " + str(e))
            return False
