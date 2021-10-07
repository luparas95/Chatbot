from classes.RolePermission import get_obj as get_obj_role_permission
from classes.Artwork import get_obj as get_obj_artwork
from classes.Language import get_obj as get_obj_language

OBJET_NAME = "Artwork info"
TABLE_NAME = "ArtworkInfo"
FIELD_MAX_SIZE = {
    "Description": 500,
}


def get_obj(db, value, by_id=False):
    if by_id:
        data = db.execute('SELECT * FROM ArtworkInfo WHERE Id = ?', (value,), True)
    else:
        data = db.execute(
            'SELECT * FROM ArtworkInfo WHERE ArtworkId = ? AND LanguageId = ?', (value[0], value[1]), True
        )

    if data is None:
        return None

    obj = ArtworkInfo(
        data[1],
        data[2],
        data[3],
    )
    obj.set_id(data[0])

    return obj


def get_nb_rows(db):
    return db.get_nb_rows('SELECT COUNT(*) FROM ArtistInfo')


def get_all_rows(db):
    return db.get_all_rows('SELECT * FROM ArtistInfo')


class ArtworkInfo:

    def __init__(self, artwork, language, description):
        self.__id = None
        self.__artwork = artwork
        self.__language = language
        self.__description = description
        self.__message = ''

    # Getters
    def get_id(self):
        return self.__id

    def get_artwork(self):
        return self.__artwork

    def get_language(self):
        return self.__language

    def get_description(self):
        return self.__description

    def get_message(self):
        return self.__message

    # Setters
    def set_id(self, value):
        self.__id = value

    def set_artwork(self, value):
        self.__artwork = value

    def set_language(self, value):
        self.__language = value

    def set_description(self, value):
        self.__description = value

    def set_message(self, value):
        self.__message = value

    # Methods
    def __append_message(self, value):
        self.__message += value

    def __validate_artwork(self, db):
        artwork = get_obj_artwork(db, self.get_artwork(), True)
        if self.get_artwork() == '':
            self.__append_message("Artwork cannot be empty.\n")
        elif artwork is None:
            artwork = get_obj_artwork(db, self.get_artwork())
            if artwork is None:
                self.__append_message("Artwork not exist.\n")
            else:
                self.set_artwork(artwork.get_id())

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

    def __validate_description(self):
        if self.get_description() == '':
            self.__append_message("Description cannot be empty.\n")
        elif len(self.get_description()) > FIELD_MAX_SIZE["Description"]:
            self.__append_message("Description cannot exceed " + str(FIELD_MAX_SIZE["Description"]) + " characters.\n")

    def __exist(self, db):
        return get_obj(db, self.get_id(), True) is not None

    def __is_valid(self, db):
        self.set_message('')
        artwork_info = get_obj(db, self.get_id(), True)
        if not artwork_info.__exist(db) or (artwork_info.__exist(db) and
                                            (artwork_info.get_artwork() != self.get_artwork() or
                                             artwork_info.get_language() != self.get_language())):
            self.__validate_artwork(db)
            self.__validate_language(db)
            if self.__exist(db):
                self.__append_message(OBJET_NAME + " already exist.\n")
        self.__validate_description()

        if self.get_message() == '':
            self.set_message(OBJET_NAME + " valid.")
            return True

        return False

    def insert(self, db, user):
        if get_obj_role_permission(db, [user.get_role, "Insert"]) is not None:
            if self.__is_valid(db):
                data = [
                    self.get_artwork(),
                    self.get_language(),
                    self.get_description(),
                ]
                db.execute(
                    'INSERT INTO ArtistInfo VALUES (NULL, ?, ?, ?, ?, current_timestamp, ?, current_timestamp)',
                    (data, user.get_id(), user.get_id(),)
                )
                self.set_message(OBJET_NAME + " inserted.")
        else:
            self.set_message("The user does not have permission to insert records into " + TABLE_NAME + " table.")

    def update(self, db, user):
        if get_obj_role_permission(db, [user.get_role, "Update"]) is not None:
            if self.__is_valid(db):
                data = [
                    self.get_artwork(),
                    self.get_language(),
                    self.get_description(),
                ]
                db.execute('''
                    UPDATE ArtistInfo SET 
                    ArtworkId = ?, LanguageId = ?, Description = ?, UpdateUserId = ?, UpdateDate = current_timestamp 
                    WHERE Id = ?
                ''', (data, user.get_id(), self.get_id(),))
                self.set_message(OBJET_NAME + " updated.")
        else:
            self.set_message("The user does not have permission to update records from " + TABLE_NAME + " table.")

    def delete(self, db, user):
        if get_obj_role_permission(db, [user.get_role, "Delete"]) is not None:
            if self.__exist(db):
                db.execute('DELETE FROM ArtistInfo WHERE Id = ?', self.get_id())
                self.set_message(OBJET_NAME + " deleted.")
            else:
                self.set_message(OBJET_NAME + " not exist.")
        else:
            self.set_message("The user does not have permission to delete records from " + TABLE_NAME + " table.")

    def print(self, db):
        artwork = get_obj_artwork(db, self.get_artwork(), True)
        language = get_obj_language(db, self.get_language(), True)

        print(OBJET_NAME.upper() + " DATA (" + str(self.get_id()) + ")")
        print("Artwork: " + artwork.get_name())
        print("Language: " + language.get_name())
        print("Description: " + self.get_description())
