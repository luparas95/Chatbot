from classes.RolePermission import get_obj as get_obj_role_permission
from classes.Nationality import get_obj as get_obj_nationality
from datetime import datetime

OBJECT_NAME = "Artist"
TABLE_NAME = "Artist"
FIELD_MAX_SIZE = {
    "Name": 30,
    "Last name": 30,
}


def get_obj(db, value, by_id=False):
    if by_id:
        data = db.execute('SELECT * FROM Artist WHERE Id = ?', (value,), True)
    else:
        data = db.execute('SELECT * FROM Artist WHERE LastName = ?', (value,), True)

    if data is None:
        return None

    obj = Artist(
        data[1],
        data[2],
        data[3],
        data[4],
        data[5],
    )
    obj.set_id(data[0])

    return obj


def get_nb_rows(db):
    return db.get_nb_rows('SELECT COUNT(*) FROM Artist')


def get_all_rows(db):
    return db.get_all_rows('SELECT * FROM Artist')


def get_name_list(db, nlp):
    rows = get_all_rows(db)
    names = []

    for row in rows:
        doc = nlp(row[1].lower())
        names.append(str(doc))
        doc = nlp(row[2].lower())
        if len(doc) > 1:
            for i in range(len(doc) - 1):
                names.append(str(doc[i]))

    return names


def get_last_name_list(db, nlp):
    rows = get_all_rows(db)
    last_names = []

    for row in rows:
        doc = nlp(row[2].lower())
        last_names.append(str(doc[-1]))

    return last_names


def srch_by_last_name(db, nlp, value):
    rows = get_all_rows(db)
    obj = None

    for row in rows:
        doc = nlp(row[2].lower())
        if str(doc[-1]) is value:
            obj = Artist(
                row[1],
                row[2],
                row[3],
                row[4],
                row[5],
            )
            obj.set_id(row[0])
            break

    return obj


def valid_date(date):
    try:
        datetime.strptime(date, '%Y-%m-%d')
        return True
    except ValueError:
        return False


class Artist:

    def __init__(self, name, last_name, bron_date, death_date, nationality):
        self.__id = None
        self.__name = name
        self.__last_name = last_name
        self.__bron_date = bron_date
        self.__death_date = death_date
        self.__nationality = nationality
        self.__message = ''

    # Getters
    def get_id(self):
        return self.__id

    def get_name(self):
        return self.__name

    def get_last_name(self):
        return self.__last_name

    def get_born_date(self):
        return self.__bron_date

    def get_death_date(self):
        return self.__death_date

    def get_nationality(self):
        return self.__nationality

    def get_message(self):
        return self.__message

    # Setters
    def set_id(self, value):
        self.__id = value

    def set_name(self, value):
        self.__name = value

    def set_last_name(self, value):
        self.__last_name = value

    def set_bron_date(self, value):
        self.__bron_date = value

    def set_death_date(self, value):
        self.__death_date = value

    def set_nationality(self, value):
        self.__nationality = value

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

    def __validate_last_name(self):
        if self.get_last_name() == '':
            self.__append_message("Last name cannot be empty.\n")
        elif len(self.get_last_name()) > FIELD_MAX_SIZE["Last name"]:
            self.__append_message("Last name cannot exceed " + str(FIELD_MAX_SIZE["Last name"]) + " characters.\n")

    def __validate_born_date(self):
        if self.get_born_date() == '':
            self.__append_message("Born date cannot be empty.\n")
        elif not valid_date(self.get_born_date()):
            self.__append_message("Format of born date must be YYYY-MM-DD.\n")
        elif self.get_born_date() > datetime.today().strftime('%Y-%m-%d'):
            self.__append_message("Born date must be less than the current date.\n")

    def __validate_death_date(self):
        if self.get_born_date() != '':
            if not valid_date(self.get_born_date()):
                self.__append_message("Format of the death date must be YYYY-MM-DD.\n")
            elif self.get_born_date() > datetime.today().strftime('%Y-%m-%d'):
                self.__append_message("Death date must be less than the current date.\n")

    def __validate_nationality(self, db):
        nationality = get_obj_nationality(db, self.get_nationality(), True)
        if self.get_nationality() == '':
            self.__append_message("Nationality cannot be empty.\n")
        elif nationality is None:
            nationality = get_obj_nationality(db, self.get_nationality())
            if nationality is None:
                self.__append_message("Nationality not exist.\n")
            else:
                self.set_nationality(nationality.get_id())

    def __exist(self, db):
        return get_obj(db, self.get_id(), True) is not None

    def __is_valid(self, db):
        self.set_message('')
        artist = get_obj(db, self.get_id(), True)
        if not artist.__exist(db) or (artist.__exist(db) and artist.get_last_name() != self.get_last_name()):
            self.__validate_name()
            self.__validate_last_name()
            if self.__exist(db):
                self.__append_message(OBJECT_NAME + " already exist.\n")
        self.__validate_born_date()
        self.__validate_death_date()
        self.__validate_nationality(db)

        if self.get_message() == '':
            self.set_message(OBJECT_NAME + " valid.")
            return True

        return False

    def insert(self, db, user):
        if get_obj_role_permission([user.get_role, "Insert"], db) is not None:
            if self.__is_valid(db):
                data = [
                    self.get_name(),
                    self.get_last_name(),
                    self.get_born_date(),
                    self.get_death_date(),
                    self.get_nationality(),
                ]
                db.execute(
                    'INSERT INTO Artist VALUES (NULL, ?, ?, ?, ?, ?, ?, current_timestamp, ?, current_timestamp)',
                    (data, user.get_id(), user.get_id(),)
                )
                self.set_message(OBJECT_NAME + " inserted.")
        else:
            self.set_message("The user does not have permission to insert records into " + TABLE_NAME + " table.")

    def update(self, db, user):
        if get_obj_role_permission([user.get_role, "Update"], db) is not None:
            if self.__is_valid(db):
                data = [
                    self.get_name(),
                    self.get_last_name(),
                    self.get_born_date(),
                    self.get_death_date(),
                    self.get_nationality(),
                ]
                db.execute('''
                    UPDATE Artist SET 
                    Name = ?, LastName = ?, BornDate = ?, DeathDate = ?, NationalityId = ?, UpdateUserId = ?, 
                    UpdateDate = current_timestamp 
                    WHERE Id = ?
                ''', (data, user.get_id(), self.get_id(),))
                self.set_message(OBJECT_NAME + " updated.")
        else:
            self.set_message("The user does not have permission to update records from " + TABLE_NAME + " table.")

    def delete(self, db, user):
        if get_obj_role_permission(db, [user.get_role, "Delete"]) is not None:
            if self.__exist(db):
                db.execute('DELETE FROM Artist WHERE Id = ?', self.get_id())
                self.set_message(OBJECT_NAME + " deleted.")
            else:
                self.set_message(OBJECT_NAME + " not exist.")
        else:
            self.set_message("The user does not have permission to delete records from " + TABLE_NAME + " table.")

    def print(self, db):
        nationality = get_obj_nationality(db, self.get_nationality(), True)

        print(OBJECT_NAME.upper() + " DATA (" + str(self.get_id()) + ")")
        print("Name: " + self.get_name())
        print("Last name: " + self.get_last_name())
        print("Born date: " + self.get_born_date())
        print("Death date: " + self.get_death_date())
        print("Nationality: " + nationality.get_name())
