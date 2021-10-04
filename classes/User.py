from classes.RolePermission import get_obj as get_obj_role_permission
from classes.Role import get_obj as get_obj_role

OBJECT_NAME = "User"
TABLE_NAME = "User"
FIELD_MAX_SIZE = {
    "Nick": 30,
    "Password": 102,
    "Name": 30,
    "Last name": 30,
}


def get_obj(db, value, by_id=False):
    if by_id:
        data = db.execute('SELECT * FROM User WHERE Id = ?', (value,), True)
    else:
        data = db.execute('SELECT * FROM User WHERE Nick = ?', (value,), True)

    if data is None:
        return None

    obj = User(
        data[1],
        data[2],
        data[3],
        data[4],
        data[5],
    )
    obj.set_id(data[0])

    return obj


def get_nb_rows(db):
    return db.get_nb_rows('SELECT COUNT(*) FROM User')


def get_all_rows(db):
    return db.get_all_rows('SELECT * FROM User')


def login(db, nick, password):
    data = db.execute('SELECT * FROM User WHERE Nick = ? AND Password = ?', (nick, password,), True)

    if data is None:
        return None

    obj = User(
        data[1],
        data[2],
        data[3],
        data[4],
        data[5],
    )
    obj.set_id(data[0])

    return obj


class User:

    def __init__(self, nick, password, name, last_name, role):
        self.__id = None
        self.__nick = nick
        self.__pasword = password
        self.__name = name
        self.__last_name = last_name
        self.__role = role
        self.__message = ''

    # Getters
    def get_id(self):
        return self.__id

    def get_nick(self):
        return self.__nick

    def get_password(self):
        return self.__pasword

    def get_name(self):
        return self.__name

    def get_last_name(self):
        return self.__last_name

    def get_role(self):
        return self.__role

    def get_message(self):
        return self.__message

    # Setters
    def set_id(self, value):
        self.__id = value

    def set_nick(self, value):
        self.__nick = value

    def set_password(self, value):
        self.__pasword = value

    def set_name(self, value):
        self.__name = value

    def set_last_name(self, value):
        self.__last_name = value

    def set_role(self, value):
        self.__role = value

    def set_message(self, value):
        self.__message = value

    # Methods
    def __append_message(self, value):
        self.__message += value

    def __validate_nick(self):
        if self.get_nick() == '':
            self.__append_message("Nick cannot be empty.\n")
        elif len(self.get_nick()) > FIELD_MAX_SIZE["Nick"]:
            self.__append_message("Nick cannot exceed " + str(FIELD_MAX_SIZE["Nick"]) + " characters.\n")
        elif not self.get_nick().islower():
            self.__append_message("Nick can only contain lower case characters.\n")
        elif self.get_nick().count(' ') > 0:
            self.__append_message("Nick cannot contain spaces.\n")

    def __validate_password(self):
        if self.get_password() == '':
            self.__append_message("Password cannot be empty.\n")
        elif len(self.get_password()) > FIELD_MAX_SIZE["Password"]:
            self.__append_message("Password cannot exceed " + str(FIELD_MAX_SIZE["Password"]) + " characters.\n")

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

    def __validate_role(self, db):
        role = get_obj_role(db, self.get_role(), True)
        if self.get_role() == '':
            self.__append_message("Role cannot be empty.\n")
        elif role is None:
            role = get_obj_role(db, self.get_role())
            if role is None:
                self.__append_message("Role not exist.\n")
            else:
                self.set_role(role.get_id())

    def __exist(self, db):
        return get_obj(db, self.get_id(), True) is not None

    def __is_valid(self, db):
        self.set_message('')
        user = get_obj(db, self.get_id(), True)
        if not user.__exist(db) or (user.__exist(db) and user.get_nick() != self.get_nick()):
            self.__validate_nick()
            if self.__exist(db):
                self.__append_message("Nick already exist.\n")
        self.__validate_password()
        self.__validate_name()
        self.__validate_last_name()
        self.__validate_role(db)

        if self.get_message() == '':
            self.set_message(OBJECT_NAME + " valid.")
            return True

        return False

    def insert(self, db, user):
        if get_obj_role_permission(db, [user.get_role, "Insert"]) is not None:
            if self.__is_valid(db):
                data = [
                    self.get_nick(),
                    self.get_password(),
                    self.get_name(),
                    self.get_last_name(),
                    self.get_role()
                ]
                db.execute(
                    'INSERT INTO User VALUES (NULL, ?, ?, ?, ?, ?, ?, current_timestamp, ?, current_timestamp)',
                    (data, user.get_id(), user.get_id(),)
                )
                self.set_message(OBJECT_NAME + " inserted.")
        else:
            self.set_message("The user does not have permission to insert records into " + TABLE_NAME + " table.")

    def update(self, db, user):
        if get_obj_role_permission(db, [user.get_role, "Update"]) is not None:
            if self.__is_valid(db):
                data = [
                    self.get_nick(),
                    self.get_password(),
                    self.get_name(),
                    self.get_last_name(),
                    self.get_role()
                ]
                db.execute('''
                    UPDATE User SET 
                    Nick = ?, Password = ?, Name = ?, LastName = ?, RoleId = ?, UpdateUserId = ?, 
                    UpdateDate = current_timestamp 
                    WHERE Id = ?
                ''', (data, user.get_id(), self.get_id(),))
                self.set_message(OBJECT_NAME + " updated.")
        else:
            self.set_message("The user does not have permission to update records from " + TABLE_NAME + " table.")

    def delete(self, db, user):
        if get_obj_role_permission(db, [user.get_role, "Delete"]) is not None:
            if user.get_id() != self.get_id():
                if self.__exist(db):
                    db.execute('DELETE FROM User WHERE Id = ?', self.get_id())
                    self.set_message(OBJECT_NAME + " deleted.")
                else:
                    self.set_message(OBJECT_NAME + " not exist.")
            else:
                self.set_message("A " + OBJECT_NAME + " cannot delete himself.")
        else:
            self.set_message("The user does not have permission to delete records from " + TABLE_NAME + " table.")

    def print(self, db):
        role = get_obj_role(db, self.get_role(), True)

        print(OBJECT_NAME.upper() + " DATA (" + self.get_id() + ")")
        print("Nick: " + self.get_nick())
        print("Name: " + self.get_name())
        print("Last name: " + self.get_last_name())
        print("Role: " + role.get_name())
