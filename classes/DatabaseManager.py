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
    def execute(self, query, parameters, is_select=False):
        self.get_cursor().execute(query, parameters)

        if is_select:
            return self.get_cursor().fetchone()
        else:
            self.commit()

    def get_nb_rows(self, query):
        self.get_cursor().execute(query)
        return self.get_cursor().fetchone()

    def get_all_rows(self, query):
        self.get_cursor().execute(query)
        return self.get_cursor().fetchall()

    def commit(self):
        self.get_db().commit()

    def close_conn(self):
        self.get_db().close()
