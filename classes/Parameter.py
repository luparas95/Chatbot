from classes.RolePermission import get_obj as get_obj_role_permission

OBJET_NAME = "Parameter"
TABLE_NAME = "Parameter"
FIELD_MAX_SIZE = {
    "Key": 30,
    "Value": 500,
}


def get_obj(db, value, by_id=False):
    if by_id:
        data = db.execute('SELECT * FROM Parameter WHERE Id = ?', (value,), True)
    else:
        data = db.execute('SELECT * FROM Parameter WHERE Key = ?', (value,), True)

    if data is None:
        return None

    obj = Parameter(
        data[1],
        data[2],
    )
    obj.set_id(data[0])

    return obj


def get_nb_rows(db):
    return db.get_nb_rows('SELECT COUNT(*) FROM Parameter')


def get_all_rows(db):
    return db.get_all_rows('SELECT * FROM Parameter')


class Parameter:

    def __init__(self, key, value):
        self.__id = None
        self.__key = key
        self.__value = value
        self.__message = ''

    # Getters
    def get_id(self):
        return self.__id

    def get_key(self):
        return self.__key

    def get_value(self):
        return self.__value

    def get_message(self):
        return self.__message

    # Setters
    def set_id(self, value):
        self.__id = value

    def set_key(self, value):
        self.__key = value

    def set_value(self, value):
        self.__value = value

    def set_message(self, value):
        self.__message = value

    # Methods
    def __append_message(self, value):
        self.__message += value

    def __validate_key(self):
        if self.get_key() == '':
            self.__append_message("Key cannot be empty.\n")
        elif len(self.get_key()) > FIELD_MAX_SIZE["Key"]:
            self.__append_message("Key cannot exceed " + str(FIELD_MAX_SIZE["Key"]) + " characters.\n")

    def __validate_value(self):
        if self.get_value() == '':
            self.__append_message("Value cannot be empty.\n")
        elif len(self.get_value()) > FIELD_MAX_SIZE["Value"]:
            self.__append_message("Value cannot exceed " + str(FIELD_MAX_SIZE["Value"]) + " characters.\n")

    def __exist(self, db):
        return get_obj(db, self.get_id(), True) is not None

    def __is_valid(self, db):
        self.set_message('')
        role = get_obj(db, self.get_id(), True)
        if not role.__exist(db) or (role.__exist(db) and role.get_key() != self.get_key()):
            self.__validate_key()
            if self.__exist(db):
                self.__append_message("Key already exist.\n")
        self.__validate_value()

        if self.get_message() == '':
            self.set_message(OBJET_NAME + " valid.")
            return True

        return False

    def insert(self, db, user):
        if get_obj_role_permission(db, [user.get_role, "Insert"]) is not None:
            if self.__is_valid(db):
                data = [
                    self.get_key(),
                    self.get_value(),
                ]
                db.execute(
                    'INSERT INTO Parameter VALUES (NULL, ?, ?, ?, current_timestamp, ?, current_timestamp)',
                    (data, user.get_id(), user.get_id(),)
                )
                self.set_message(OBJET_NAME + " inserted.")
        else:
            self.set_message("The user does not have permission to insert records into " + TABLE_NAME + " table.")

    def update(self, db, user):
        if get_obj_role_permission(db, [user.get_role, "Update"]) is not None:
            if self.__is_valid(db):
                data = [
                    self.get_key(),
                    self.get_value(),
                ]
                db.execute('''
                    UPDATE Parameter SET 
                    Key = ?, Value = ?, UpdateUserId = ?, UpdateDate = current_timestamp 
                    WHERE Id = ?
                ''', (data, user.get_id(), self.get_id(),))
                self.set_message(OBJET_NAME + " updated.")
        else:
            self.set_message("The user does not have permission to update records from " + TABLE_NAME + " table.")

    def delete(self, db, user):
        if get_obj_role_permission(db, [user.get_role, "Delete"]) is not None:
            if self.__exist(db):
                db.execute('DELETE FROM Parameter WHERE Id = ?', self.get_id())
                self.set_message(OBJET_NAME + " deleted.")
            else:
                self.set_message(OBJET_NAME + " not exist.")
        else:
            self.set_message("The user does not have permission to delete records from " + TABLE_NAME + " table.")

    def print(self):
        print(OBJET_NAME.upper() + " DATA (" + self.get_id() + ")")
        print("Key: " + self.get_key())
        print("Value: " + self.get_value())
