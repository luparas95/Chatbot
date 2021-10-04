import sqlite3
import json
from os import path, getcwd

DB_PATH = path.join(getcwd(), "chatbotBBDD.sqlite")
JSON_PATH = path.join(getcwd(), "chatbotBBDD_backup.json")


def unload_role(cursor):
    cursor.execute('SELECT * FROM "Role"')
    return cursor.fetchall()


def unload_permission(cursor):
    cursor.execute('SELECT * FROM Permission')
    return cursor.fetchall()


def unload_role_permission(cursor):
    cursor.execute('SELECT * FROM RolePermission')
    return cursor.fetchall()


def unload_user(cursor):
    cursor.execute('SELECT * FROM "User"')
    return cursor.fetchall()


def unload_nationality(cursor):
    cursor.execute('SELECT * FROM Nationality')
    return cursor.fetchall()


def unload_artist(cursor):
    cursor.execute('SELECT * FROM Artist')
    return cursor.fetchall()


def unload_artwork(cursor):
    cursor.execute('SELECT * FROM Artwork')
    return cursor.fetchall()


def unload_language(cursor):
    cursor.execute('SELECT * FROM "Language"')
    return cursor.fetchall()


def unload_artist_info(cursor):
    cursor.execute('SELECT * FROM ArtistInfo')
    return cursor.fetchall()


def unload_artwork_info(cursor):
    cursor.execute('SELECT * FROM ArtworkInfo')
    return cursor.fetchall()


def unload_parameter(cursor):
    cursor.execute('SELECT * FROM "Parameter"')
    return cursor.fetchall()


def create_json():
    connection = sqlite3.connect(DB_PATH)
    cursor = connection.cursor()

    data = {
        "Role": unload_role(cursor),
        "Permission": unload_permission(cursor),
        "RolePermission": unload_role_permission(cursor),
        "User": unload_user(cursor),
        "Nationality": unload_nationality(cursor),
        "Artist": unload_artist(cursor),
        "Artwork": unload_artwork(cursor),
        "Language": unload_language(cursor),
        "ArtistInfo": unload_artist_info(cursor),
        "ArtworkInfo": unload_artwork_info(cursor),
        "Parameter": unload_parameter(cursor),
    }

    with open(JSON_PATH, 'w') as backup_file:
        json.dump(data, backup_file, indent=4)

    connection.close()


create_json()
