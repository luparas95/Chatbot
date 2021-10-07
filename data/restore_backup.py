import sqlite3
import json
from os import path, getcwd

DB_PATH = path.join(getcwd(), "chatbotBBDD.sqlite")
JSON_PATH = path.join(getcwd(), "chatbotBBDD_backup.json")


def generate_role(cursor):
    cursor.execute('DROP TABLE IF EXISTS "Role"')

    cursor.execute('''
        CREATE TABLE "Role" (
        Id INTEGER PRIMARY KEY,
        "Name" VARCHAR(30) NOT NULL,
        InsertUserId INTEGER NOT NULL,
        InsertDate DATETIME NOT NULL,
        UpdateUserId INTEGER NOT NULL,
        UpdateDate DATETIME NOT NULL,
        UNIQUE ("Name"),
        FOREIGN KEY (InsertUserId) REFERENCES "User"(Id) ON DELETE CASCADE,
        FOREIGN KEY (UpdateUserId) REFERENCES "User"(Id) ON DELETE CASCADE)
        ''')


def generate_permission(cursor):
    cursor.execute('DROP TABLE IF EXISTS Permission')

    cursor.execute('''
        CREATE TABLE Permission (
        Id INTEGER PRIMARY KEY,
        "Name" VARCHAR(30) NOT NULL,
        InsertUserId INTEGER NOT NULL,
        InsertDate DATETIME NOT NULL,
        UpdateUserId INTEGER NOT NULL,
        UpdateDate DATETIME NOT NULL,
        UNIQUE ("Name"),
        FOREIGN KEY (InsertUserId) REFERENCES "User"(Id) ON DELETE CASCADE,
        FOREIGN KEY (UpdateUserId) REFERENCES "User"(Id) ON DELETE CASCADE)
    ''')


def generate_role_permission(cursor):
    cursor.execute('DROP TABLE IF EXISTS RolePermission')

    cursor.execute('''
        CREATE TABLE RolePermission (
        Id INTEGER PRIMARY KEY,
        RoleId INTEGER NOT NULL,
        PermissionId INTEGER NOT NULL,
        InsertUserId INTEGER NOT NULL,
        InsertDate DATETIME NOT NULL,
        UpdateUserId INTEGER NOT NULL,
        UpdateDate DATETIME NOT NULL,
        UNIQUE (RoleId, PermissionId),
        FOREIGN KEY (RoleId) REFERENCES "Role"(Id) ON DELETE CASCADE,
        FOREIGN KEY (PermissionId) REFERENCES Permission(Id) ON DELETE CASCADE,
        FOREIGN KEY (InsertUserId) REFERENCES "User"(Id) ON DELETE CASCADE,
        FOREIGN KEY (UpdateUserId) REFERENCES "User"(Id) ON DELETE CASCADE)
        ''')


def generate_user(cursor):
    cursor.execute('DROP TABLE IF EXISTS "User"')

    cursor.execute('''
        CREATE TABLE "User" (
        Id INTEGER PRIMARY KEY,
        Nick VARCHAR(30) NOT NULL,
        Password VARCHAR(102),
        "Name" VARCHAR(30) NOT NULL,
        LastName VARCHAR(30) NOT NULL,
        RoleId INTEGER NOT NULL,
        InsertUserId INTEGER NOT NULL,
        InsertDate DATETIME NOT NULL,
        UpdateUserId INTEGER NOT NULL,
        UpdateDate DATETIME NOT NULL,
        UNIQUE (Nick),
        FOREIGN KEY (RoleId) REFERENCES "Role"(Id) ON DELETE CASCADE,
        FOREIGN KEY (InsertUserId) REFERENCES "User"(Id) ON DELETE CASCADE,
        FOREIGN KEY (UpdateUserId) REFERENCES "User"(Id) ON DELETE CASCADE)
    ''')


def generate_nationality(cursor):
    cursor.execute('DROP TABLE IF EXISTS Nationality')

    cursor.execute('''
        CREATE TABLE Nationality (
        Id INTEGER PRIMARY KEY,
        "Name" VARCHAR(30) NOT NULL,
        InsertUserId INTEGER NOT NULL,
        InsertDate DATETIME NOT NULL,
        UpdateUserId INTEGER NOT NULL,
        UpdateDate DATETIME NOT NULL,
        UNIQUE ("Name"),
        FOREIGN KEY (InsertUserId) REFERENCES "User"(Id) ON DELETE CASCADE,
        FOREIGN KEY (UpdateUserId) REFERENCES "User"(Id) ON DELETE CASCADE)
    ''')


def generate_artist(cursor):
    cursor.execute('DROP TABLE IF EXISTS Artist')

    cursor.execute('''
        CREATE TABLE Artist (
        Id INTEGER PRIMARY KEY,
        "Name" VARCHAR(30) NOT NULL,
        LastName VARCHAR(30) NOT NULL,
        BornDate DATE NOT NULL,
        DeathDate DATE,
        NationalityId INTEGER NOT NULL,
        InsertUserId INTEGER NOT NULL,
        InsertDate DATETIME NOT NULL,
        UpdateUserId INTEGER NOT NULL,
        UpdateDate DATETIME NOT NULL,
        UNIQUE (LastName),
        FOREIGN KEY (NationalityId) REFERENCES Nationality(Id) ON DELETE CASCADE,
        FOREIGN KEY (InsertUserId) REFERENCES "User"(Id) ON DELETE CASCADE,
        FOREIGN KEY (UpdateUserId) REFERENCES "User"(Id) ON DELETE CASCADE)
    ''')


def generate_artwork(cursor):
    cursor.execute('DROP TABLE IF EXISTS Artwork')

    cursor.execute('''
        CREATE TABLE Artwork (
        Id INTEGER PRIMARY KEY,
        "Name" VARCHAR(30) NOT NULL,
        CreationYear YEAR NOT NULL,
        ArtistId INTEGER NOT NULL,
        InsertUserId INTEGER NOT NULL,
        InsertDate DATETIME NOT NULL,
        UpdateUserId INTEGER NOT NULL,
        UpdateDate DATETIME NOT NULL,
        UNIQUE ("Name"),
        FOREIGN KEY (ArtistId) REFERENCES Artist(Id) ON DELETE CASCADE,
        FOREIGN KEY (InsertUserId) REFERENCES "User"(Id) ON DELETE CASCADE,
        FOREIGN KEY (UpdateUserId) REFERENCES "User"(Id) ON DELETE CASCADE)
    ''')


def generate_language(cursor):
    cursor.execute('DROP TABLE IF EXISTS "Language"')

    cursor.execute('''
        CREATE TABLE "Language"(
        Id INTEGER PRIMARY KEY,
        "Name" VARCHAR(30) NOT NULL,
        InsertUserId INTEGER NOT NULL,
        InsertDate DATETIME NOT NULL,
        UpdateUserId INTEGER NOT NULL,
        UpdateDate DATETIME NOT NULL,
        UNIQUE ("Name"),
        FOREIGN KEY (InsertUserId) REFERENCES "User"(Id) ON DELETE CASCADE,
        FOREIGN KEY (UpdateUserId) REFERENCES "User"(Id) ON DELETE CASCADE)
    ''')


def generate_artist_info(cursor):
    cursor.execute('DROP TABLE IF EXISTS ArtistInfo')

    cursor.execute('''
        CREATE TABLE ArtistInfo (
        Id INTEGER PRIMARY KEY,
        ArtistId INTEGER NOT NULL,
        LanguageId INTEGER NOT NULL,
        Description VARCHAR(500) NOT NULL,
        InsertUserId INTEGER NOT NULL,
        InsertDate DATETIME NOT NULL,
        UpdateUserId INTEGER NOT NULL,
        UpdateDate DATETIME NOT NULL,
        UNIQUE (ArtistId, LanguageId),
        FOREIGN KEY (ArtistId) REFERENCES ARTIST(Id) ON DELETE CASCADE,
        FOREIGN KEY (LanguageId) REFERENCES "Language"(Id) ON DELETE CASCADE,
        FOREIGN KEY (InsertUserId) REFERENCES "User"(Id) ON DELETE CASCADE,
        FOREIGN KEY (UpdateUserId) REFERENCES "User"(Id) ON DELETE CASCADE)
    ''')


def generate_artwork_info(cursor):
    cursor.execute('DROP TABLE IF EXISTS ArtworkInfo')

    cursor.execute('''
        CREATE TABLE ArtworkInfo (
        Id INTEGER PRIMARY KEY,
        ArtworkId INTEGER NOT NULL,
        LanguageId INTEGER NOT NULL,
        Description VARCHAR(500) NOT NULL,
        InsertUserId INTEGER NOT NULL,
        InsertDate DATETIME NOT NULL,
        UpdateUserId INTEGER NOT NULL,
        UpdateDate DATETIME NOT NULL,
        UNIQUE (ArtworkId, LanguageId),
        FOREIGN KEY (ArtworkId) REFERENCES Artwork(Id) ON DELETE CASCADE,
        FOREIGN KEY (LanguageId) REFERENCES "Language"(Id) ON DELETE CASCADE,
        FOREIGN KEY (InsertUserId) REFERENCES "User"(Id) ON DELETE CASCADE,
        FOREIGN KEY (UpdateUserId) REFERENCES "User"(Id) ON DELETE CASCADE)
    ''')


def generate_parameter(cursor):
    cursor.execute('DROP TABLE IF EXISTS "Parameter"')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS "Parameter"(
        Id INTEGER PRIMARY KEY,
        "Key" VARCHAR(30) NOT NULL,
        "Value" VARCHAR(500) NOT NULL,
        InsertUserId INTEGER NOT NULL,
        InsertDate DATETIME NOT NULL,
        UpdateUserId INTEGER NOT NULL,
        UpdateDate DATETIME NOT NULL,
        UNIQUE ("Key"),
        FOREIGN KEY (InsertUserId) REFERENCES "User"(Id) ON DELETE CASCADE,
        FOREIGN KEY (UpdateUserId) REFERENCES "User"(Id) ON DELETE CASCADE)
    ''')


def insert_role(cursor, data):
    cursor.executemany('''
        INSERT INTO "Role"
        VALUES (?, ?, ?, ?, ?, ?)
    ''', data)

    print("Inserted " + str(len(data)) + " new elements in Role table.")


def insert_permission(cursor, data):
    cursor.executemany('''
        INSERT INTO Permission
        VALUES (?, ?, ?, ?, ?, ?)
    ''', data)

    print("Inserted " + str(len(data)) + " new elements in Permission table.")


def insert_role_permission(cursor, data):
    cursor.executemany('''
        INSERT INTO RolePermission
        VALUES (?, ?, ?, ?, ?, ?, ?)
    ''', data)

    print("Inserted " + str(len(data)) + " new elements in RolePermission table.")


def insert_user(cursor, data):
    cursor.executemany('''
        INSERT INTO "User"
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', data)

    print("Inserted " + str(len(data)) + " new elements in User table.")


def insert_nationality(cursor, data):
    cursor.executemany('''
        INSERT INTO Nationality
        VALUES (?, ?, ?, ?, ?, ?)

    ''', data)

    print("Inserted " + str(len(data)) + " new elements in Nationality table.")


def insert_artist(cursor, data):
    cursor.executemany('''
        INSERT INTO Artist
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', data)

    print("Inserted " + str(len(data)) + " new elements in Artist table.")


def insert_artwork(cursor, data):
    cursor.executemany('''
        INSERT INTO Artwork
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    ''', data)

    print("Inserted " + str(len(data)) + " new elements in Artwork table.")


def insert_language(cursor, data):
    cursor.executemany('''
        INSERT INTO "Language"
        VALUES (?, ?, ?, ?, ?, ?)
    ''', data)

    print("Inserted " + str(len(data)) + " new elements in Language table.")


def insert_artist_info(cursor, data):
    cursor.executemany('''
        INSERT INTO ArtistInfo
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    ''', data)

    print("Inserted " + str(len(data)) + " new elements in ArtistInfo table.")


def insert_artwork_info(cursor, data):
    cursor.executemany('''
        INSERT INTO ArtworkInfo
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    ''', data)

    print("Inserted " + str(len(data)) + " new elements in ArtworkInfo table.")


def insert_parameter(cursor, data):
    cursor.executemany('''
        INSERT INTO "Parameter"
        VALUES (?, ?, ?, ?, ?, ?, ?)
    ''', data)

    print("Inserted " + str(len(data)) + " new elements in Parameter table.")


def generate_tables(cursor):
    generate_role(cursor)
    generate_permission(cursor)
    generate_role_permission(cursor)
    generate_user(cursor)
    generate_nationality(cursor)
    generate_artist(cursor)
    generate_artwork(cursor)
    generate_language(cursor)
    generate_artist_info(cursor)
    generate_artwork_info(cursor)
    generate_parameter(cursor)


def insert_registers(cursor, data):
    insert_role(cursor, data["Role"])
    insert_permission(cursor, data["Permission"])
    insert_role_permission(cursor, data["RolePermission"])
    insert_user(cursor, data["User"])
    insert_nationality(cursor, data["Nationality"])
    insert_artist(cursor, data["Artist"])
    insert_artwork(cursor, data["Artwork"])
    insert_language(cursor, data["Language"])
    insert_artist_info(cursor, data["ArtistInfo"])
    insert_artwork_info(cursor, data["ArtworkInfo"])
    insert_parameter(cursor, data["Parameter"])


def main():
    with open(JSON_PATH) as backup_file:
        data = json.load(backup_file)

    connection = sqlite3.connect(DB_PATH)
    cursor = connection.cursor()

    generate_tables(cursor)
    insert_registers(cursor, data)

    connection.commit()
    connection.close()


main()
