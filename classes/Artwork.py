from classes.RolePermission import get_obj as get_obj_role_permission
from classes.Artist import get_obj as get_obj_artist
from datetime import datetime

OBJECT_NAME = "Artwork"
TABLE_NAME = "Artwork"
FIELD_MAX_SIZE = {
    "Name": 30,
}


def get_obj(db, value, by_id=False):
    if by_id:
        data = db.execute('SELECT * FROM Artwork WHERE Id = ?', (value,), True)
    else:
        data = db.execute('SELECT * FROM Artwork WHERE Name = ?', (value,), True)

    if data is None:
        return None

    obj = Artwork(
        data[1],
        data[2],
        data[3],
    )
    obj.set_id(data[0])

    return obj


def get_nb_rows(db):
    return db.get_nb_rows('SELECT COUNT(*) FROM Artwork')


def get_all_rows(db):
    return db.get_all_rows('SELECT * FROM Artwork')


def get_name_list(db, nlp):
    rows = get_all_rows(db)
    names = []

    for row in rows:
        doc = nlp(row[1].lower())
        names.append(str(doc[-1]))

    return names


def srch_by_name(db, nlp, value):
    rows = get_all_rows(db)
    obj = None

    for row in rows:
        doc = nlp(row[1].lower())
        if str(doc[-1]) is value:
            obj = Artwork(
                row[1],
                row[2],
                row[3],
            )
            obj.set_id(row[0])
            break

    return obj


def valid_year(date):
    try:
        datetime.strptime(date, '%Y')
        return True
    except ValueError:
        return False


class Artwork:

    def __init__(self, name, creation_year, artist):
        self.__id = None
        self.__name = name
        self.__creation_year = creation_year
        self.__artist = artist
        self.__message = ''

    # Getters
    def get_id(self):
        return self.__id

    def get_name(self):
        return self.__name

    def get_creation_year(self):
        return self.__creation_year

    def get_artist(self):
        return self.__artist

    def get_message(self):
        return self.__message

    # Setters
    def set_id(self, value):
        self.__id = value

    def set_name(self, value):
        self.__name = value

    def set_creation_year(self, value):
        self.__creation_year = value

    def set_artist(self, value):
        self.__artist = value

    def set_message(self, value):
        self.__message = value

    # Methods
    def __append_message(self, value):
        self.__message += value

    def __validate_name(self):
        if self.get_name() == '':
            self.__append_message("Name cannot be empty.\n")
        elif len(self.get_name()) > FIELD_MAX_SIZE["Name"]:
            self.__append_message("Name cannot exceed " + str(FIELD_MAX_SIZE["Name"]) + " characters.\n")

    def __validate_creation_year(self):
        if self.get_creation_year() == '':
            self.__append_message("Creation year cannot be empty.\n")
        elif not valid_year(self.get_creation_year()):
            self.__append_message("Format of creation year must be YYYY.\n")
        elif self.get_creation_year() >= datetime.today().strftime('%Y'):
            self.__append_message("Creation year must be less or equal than the current year.\n")

    def __validate_artist(self, db):
        artist = get_obj_artist(db, self.get_artist(), True)
        if self.get_artist() == '':
            self.__append_message("Artist cannot be empty.\n")
        elif artist is None:
            artist = get_obj_artist(db, self.get_artist())
            if artist is None:
                self.__append_message("Artist not exist.\n")
            else:
                self.set_artist(artist.get_id())

    def __exist(self, db):
        return get_obj(db, self.get_id(), True) is not None

    def __is_valid(self, db):
        self.set_message('')
        artwork = get_obj(db, self.get_id(), True)
        if not artwork.__exist(db) or (artwork.__exist(db) and artwork.get_name() != self.get_name()):
            self.__validate_name()
            if self.__exist(db):
                self.__append_message("Name already exist.\n")
        self.__validate_creation_year()
        self.__validate_artist(db)

        if self.get_message() == '':
            self.set_message(OBJECT_NAME + " valid.")
            return True

        return False

    def insert(self, db, user):
        if get_obj_role_permission(db, [user.get_role, "Insert"]) is not None:
            if self.__is_valid(db):
                data = [
                    self.get_name(),
                    self.get_creation_year(),
                    self.get_artist(),
                ]
                db.execute(
                    'INSERT INTO Artwork VALUES (NULL, ?, ?, ?, ?, current_timestamp, ?, current_timestamp)',
                    (data, user.get_id(), user.get_id(),)
                )
                self.set_message(OBJECT_NAME + " inserted.")
        else:
            self.set_message("The user does not have permission to insert records into " + TABLE_NAME + " table.")

    def update(self, db, user):
        if get_obj_role_permission(db, [user.get_role, "Update"]) is not None:
            if self.__is_valid(db):
                data = [
                    self.get_name(),
                    self.get_creation_year(),
                    self.get_artist(),
                ]
                db.execute('''
                    UPDATE Artwork SET 
                    Name = ?, CreationYear = ?, ArtistId = ?, UpdateUserId = ?, UpdateDate = current_timestamp 
                    WHERE Id = ?
                ''', (data, user.get_id(), self.get_id(),))
                self.set_message(OBJECT_NAME + " updated.")
        else:
            self.set_message("The user does not have permission to update records from " + TABLE_NAME + " table.")

    def delete(self, db, user):
        if get_obj_role_permission(db, [user.get_role, "Delete"]) is not None:
            if self.__exist(db):
                db.execute('DELETE FROM Artwork WHERE Id = ?', self.get_id())
                self.set_message(OBJECT_NAME + " deleted.")
            else:
                self.set_message(OBJECT_NAME + " not exist.")
        else:
            self.set_message("The user does not have permission to delete records from " + TABLE_NAME + " table.")

    def print(self, db):
        artist = get_obj_artist(db, self.get_artist(), True)

        print(OBJECT_NAME.upper() + " DATA (" + str(self.get_id()) + ")")
        print("Name: " + self.get_name())
        print("Creation year: " + self.get_creation_year())
        print("Artist: " + artist.get_name())
