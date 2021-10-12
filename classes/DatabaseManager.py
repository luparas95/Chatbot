import sqlite3
from os import path, getcwd

DATABASE_PATH = path.join(getcwd(), "data/chatbotBBDD.sqlite")


class DatabaseManager:

    def __init__(self):
        try:
            self.__db = sqlite3.connect(DATABASE_PATH)
            self.__cursor = self.__db.cursor()

        except Exception as err:
            print("Error connecting to database: " + str(err))
            self.__db.close()

    # Getters
    def get_db(self):
        return self.__db

    def get_cursor(self):
        return self.__cursor

    # Setters
    def set_db(self, value):
        self.__db = value

    def set_cursor(self, value):
        self.__cursor = value

    # Methods
    def execute(self, mode, query, parameters=''):
        self.get_cursor().execute(query, parameters)
        if mode == 1:
            return self.get_cursor().fetchone()
        elif mode == 2:
            return self.get_cursor().fetchall()
        elif mode == 3:
            self.get_db().commit()
