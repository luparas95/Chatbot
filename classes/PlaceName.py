from classes.RolePermission import get_obj as get_obj_role_permission
from classes.Place import get_obj as get_obj_place
from classes.Language import get_obj as get_obj_language

OBJECT_NAME = "Name place"
TABLE_NAME = "PlaceName"
FIELD_MAX_SIZE = {
    "Name": 30,
}


def get_obj(db, value, by_id=False):
    if by_id:
        data = db.execute(1, 'SELECT * FROM PlaceName WHERE Id = ?', (value,))
    else:
        data = db.execute(1, 'SELECT * FROM PlaceName WHERE LanguageId = ? AND Name = ?', (value[0], value[1]))

    if data is None:
        return None

    obj = PlaceName(data[1], data[2], data[3])
    obj.set_id(data[0])

    return obj


def get_nb_rows(db):
    return db.execute(1, 'SELECT COUNT(*) FROM PlaceName')


def get_all_rows(db):
    return db.execute(2, 'SELECT * FROM PlaceName')


def get_name_list(db, language):
    rows = get_all_rows(db)
    language_id = get_obj_language(db, language).get_id()
    names = []

    for row in rows:
        if language_id == row[2]:
            names.append(row[3].lower())

    return names


class PlaceName:

    def __init__(self, place, language, name):
        self.__id = None
        self.__place = place
        self.__language = language
        self.__name = name
        self.__message = ''

    # Getters
    def get_id(self):
        return self.__id

    def get_place(self):
        return self.__place

    def get_language(self):
        return self.__language

    def get_name(self):
        return self.__name

    def get_message(self):
        return self.__message

    # Setters
    def set_id(self, value):
        self.__id = value

    def set_place(self, value):
        self.__place = value

    def set_language(self, value):
        self.__language = value

    def set_name(self, value):
        self.__name = value

    def set_message(self, value):
        self.__message = value

    # Methods
    def __append_message(self, value):
        self.__message += value

    def __validate_place(self, db):
        place = get_obj_place(db, self.get_place(), True)
        if self.get_place() == '':
            self.__append_message("Place cannot be empty.\n")
        elif place is None:
            place = get_obj_place(self.get_place(), db)
            if place is None:
                self.__append_message("Place not exist.\n")
            else:
                self.set_place(place.get_id())

    def __validate_language(self, db):
        language = get_obj_language(db, self.get_language(), True)
        if self.get_language() == '':
            self.__append_message("Language cannot be empty.\n")
        elif language is None:
            language = get_obj_language(db, self.get_language())
            if language is None:
                self.__append_message("Language not exist.\n")
            else:
                self.set_language(language.get_id())

    def __validate_name(self):
        if self.get_name() == '':
            self.__append_message("Description cannot be empty.\n")
        elif len(self.get_name()) > FIELD_MAX_SIZE["Name"]:
            self.__append_message("Name cannot exceed " + str(FIELD_MAX_SIZE["Name"]) + " characters.\n")

    def __exist(self, db):
        return get_obj(db, self.get_id(), True) is not None

    def __is_valid(self, db):
        self.set_message('')
        place_name = get_obj(db, self.get_id(), True)
        if not place_name.__exist(db) or (place_name.__exist(db) and
                                          (place_name.get_place() != self.get_place() or
                                           place_name.get_language() != self.get_language())):
            self.__validate_place(db)
            self.__validate_language(db)
            if get_obj(db, (self.get_place(), self.get_language())) is not None:
                self.__append_message(OBJECT_NAME + " already exist.\n")
        self.__validate_name()

        if self.get_message() == '':
            self.set_message(OBJECT_NAME + " valid.")
            return True

        return False

    def insert(self, db, user):
        if get_obj_role_permission([user.get_role, "Insert"], db) is not None:
            if self.__is_valid(db):
                data = [
                    self.get_place(),
                    self.get_language(),
                    self.get_name(),
                ]
                db.execute(
                    3, 'INSERT INTO PlaceName VALUES (NULL, ?, ?, ?, ?, current_timestamp, ?, current_timestamp)',
                    (data, user.get_id(), user.get_id(),)
                )
                self.set_message(OBJECT_NAME + " inserted.")
        else:
            self.set_message("The user does not have permission to insert records into " + TABLE_NAME + " table.")

    def update(self, db, user):
        if get_obj_role_permission(db, [user.get_role, "Update"]) is not None:
            if self.__is_valid(db):
                data = [
                    self.get_place(),
                    self.get_language(),
                    self.get_name(),
                ]
                db.execute(
                    3, '''
                    UPDATE PlaceName SET 
                    PlaceId = ?, LanguageId = ?, Name = ?, UpdateUserId = ?, UpdateDate = current_timestamp 
                    WHERE Id = ?
                    ''', (data, user.get_id(), self.get_id(),)
                )
                self.set_message(OBJECT_NAME + " updated.")
        else:
            self.set_message("The user does not have permission to update records from " + TABLE_NAME + " table.")

    def delete(self, db, user):
        if get_obj_role_permission(db, [user.get_role, "Delete"]) is not None:
            if self.__exist(db):
                db.execute(3, 'DELETE FROM PlaceName WHERE Id = ?', self.get_id())
                self.set_message(OBJECT_NAME + " deleted.")
            else:
                self.set_message(OBJECT_NAME + " not exist.")
        else:
            self.set_message("The user does not have permission to delete records from " + TABLE_NAME + " table.")

    def print(self, db):
        place = get_obj_place(db, self.get_place(), True)
        language = get_obj_language(db, self.get_language(), True)

        print(OBJECT_NAME.upper() + " DATA (" + str(self.get_id()) + ")")
        print("Place: " + place.get_x_coordinate() + ", " + place.get_y_coordinate())
        print("Language: " + language.get_name())
        print("Name: " + self.get_name())
