from classes.RolePermission import get_obj as get_obj_role_permission
from classes.Artist import get_obj as get_obj_artist
from classes.Language import get_obj as get_obj_language

OBJET_NAME = "Artist info"
TABLE_NAME = "ArtistInfo"
FIELD_MAX_SIZE = {
    "Description": 500,
}


def get_obj(db, value, by_id=False):
    if by_id:
        data = db.execute('SELECT * FROM ArtistInfo WHERE Id = ?', (value,), True)
    else:
        data = db.execute('SELECT * FROM ArtistInfo WHERE ArtistId = ? AND LanguageId = ?', (value[0], value[1]), True)

    if data is None:
        return None

    obj = ArtistInfo(
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


class ArtistInfo:

    def __init__(self, artist, language, description):
        self.__id = None
        self.__artist = artist
        self.__language = language
        self.__description = description
        self.__message = ''

    # Getters
    def get_id(self):
        return self.__id

    def get_artist(self):
        return self.__artist

    def get_language(self):
        return self.__language

    def get_description(self):
        return self.__description

    def get_message(self):
        return self.__message

    # Setters
    def set_id(self, value):
        self.__id = value

    def set_artist(self, value):
        self.__artist = value

    def set_language(self, value):
        self.__language = value

    def set_description(self, value):
        self.__description = value

    def set_message(self, value):
        self.__message = value

    # Methods
    def __append_message(self, value):
        self.__message += value

    def __validate_artist(self, db):
        artist = get_obj_artist(db, self.get_artist(), True)
        if self.get_artist() == '':
            self.__append_message("Artist cannot be empty.\n")
        elif artist is None:
            artist = get_obj_artist(self.get_artist(), db)
            if artist is None:
                self.__append_message("Artist not exist.\n")
            else:
                self.set_artist(artist.get_id())

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
        artist_info = get_obj(db, self.get_id(), True)
        if not artist_info.__exist(db) or (artist_info.__exist(db) and
                                           (artist_info.get_artist() != self.get_artist() or
                                            artist_info.get_language() != self.get_language())):
            self.__validate_artist(db)
            self.__validate_language(db)
            if self.__exist(db):
                self.__append_message(OBJET_NAME + " already exist.\n")
        self.__validate_description()

        if self.get_message() == '':
            self.set_message(OBJET_NAME + " valid.")
            return True

        return False

    def insert(self, db, user):
        if get_obj_role_permission([user.get_role, "Insert"], db) is not None:
            if self.__is_valid(db):
                data = [
                    self.get_artist(),
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
                    self.get_artist(),
                    self.get_language(),
                    self.get_description(),
                ]
                db.execute('''
                    UPDATE ArtistInfo SET 
                    ArtistId = ?, LanguageId = ?, Description = ?, UpdateUserId = ?, UpdateDate = current_timestamp 
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
        artist = get_obj_artist(db, self.get_artist(), True)
        language = get_obj_language(db, self.get_language(), True)

        print(OBJET_NAME.upper() + " DATA (" + str(self.get_id()) + ")")
        print("Artist: " + artist.get_name() + " " + artist.get_last_name())
        print("Language: " + language.get_name())
        print("Description: " + self.get_description())
