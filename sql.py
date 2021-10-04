import sqlite3
from os import path, getcwd

database_path = path.join(getcwd(), "data/chatbotBBDD.sqlite")


def select_parameter(key):
    connection = sqlite3.connect(database_path)
    cursor = connection.cursor()

    cursor.execute('SELECT "Value" FROM "Parameter" WHERE "Key" = ?', (key,))

    data = cursor.fetchone()
    if data is None:
        value = ""
        print("Key '" + key + "' not exist in Parameter table.")
    else:
        value = data[0]

    connection.close()

    return value
