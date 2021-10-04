import classes.RolePermission as RolePermission

OBJET_NAME = "Role"
TABLE_NAME = "Role"
FIELD_MAX_SIZE = {
    "Name": 30,
}


def get_obj(db, value, by_id=False):
    if by_id:
        data = db.execute('SELECT * FROM Role WHERE Id = ?', (value,), True)
    else:
        data = db.execute('SELECT * FROM Role WHERE Name = ?', (value,), True)

    if data is None:
        return None

    obj = Role(
        data[1],
    )
    obj.set_id(data[0])

    return obj


def get_nb_rows(db):
    return db.get_nb_rows('SELECT COUNT(*) FROM Role')


def get_all_rows(db):
    return db.get_all_rows('SELECT * FROM Role')


class Role:

    def __init__(self, name):
        self.__id = None
        self.__name = name
        self.__message = ''

    # Getters
    def get_id(self):
        return self.__id

    def get_name(self):
        return self.__name

    def get_message(self):
        return self.__message

    # Setters
    def set_id(self, value):
        self.__id = value

    def set_name(self, value):
        self.__name = value

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

    def __exist(self, db):
        return get_obj(db, self.get_id(), True) is not None

    def __is_valid(self, db):
        self.set_message('')
        role = get_obj(db, self.get_id(), True)
        if not role.__exist(db) or (role.__exist(db) and role.get_name() != self.get_name()):
            self.__validate_name()
            if self.__exist(db):
                self.__append_message("Name already exist.\n")

        if self.get_message() == '':
            self.set_message(OBJET_NAME + " valid.")
            return True

        return False

    def insert(self, db, user):
        if RolePermission.get_obj(db, [user.get_role, "Insert"]) is not None:
            if self.__is_valid(db):
                data = [
                    self.get_name(),
                ]
                db.execute(
                    'INSERT INTO Role VALUES (NULL, ?, ?, current_timestamp, ?, current_timestamp)',
                    (data, user.get_id(), user.get_id(),)
                )
                self.set_message(OBJET_NAME + " inserted.")
        else:
            self.set_message("The user does not have permission to insert records into " + TABLE_NAME + " table.")

    def update(self, db, user):
        if RolePermission.get_obj(db, [user.get_role, "Update"]) is not None:
            if self.__is_valid(db):
                data = [
                    self.get_name(),
                ]
                db.execute('''
                    UPDATE Role SET 
                    Name = ?, UpdateUserId = ?, UpdateDate = current_timestamp 
                    WHERE Id = ?
                ''', (data, user.get_id(), self.get_id(),))
                self.set_message(OBJET_NAME + " updated.")
        else:
            self.set_message("The user does not have permission to update records from " + TABLE_NAME + " table.")

    def delete(self, db, user):
        if RolePermission.get_obj(db, [user.get_role, "Delete"]) is not None:
            if self.__exist(db):
                db.execute('DELETE FROM Role WHERE Id = ?', self.get_id())
                self.set_message(OBJET_NAME + " deleted.")
            else:
                self.set_message(OBJET_NAME + " not exist.")
        else:
            self.set_message("The user does not have permission to delete records from " + TABLE_NAME + " table.")

    def print(self):
        print(OBJET_NAME.upper() + " DATA (" + self.get_id() + ")")
        print("Name: " + self.get_name())
