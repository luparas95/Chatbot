from classes.Role import get_obj as get_obj_role
from classes.Permission import get_obj as get_obj_permission

OBJET_NAME = "Role permission"
TABLE_NAME = "RolePermission"
FIELD_MAX_SIZE = {}


def get_obj(db, value, by_id=False):
    if by_id:
        data = db.execute('SELECT * FROM RolePermission WHERE Id = ?', (value,), True)
    else:
        data = db.execute(
            'SELECT * FROM RolePermission WHERE RoleId = ? AND PermissionId = ?', (value[0], value[1]), True
        )

    if data is None:
        return None

    obj = RolePermission(
        data[1],
        data[2],
    )
    obj.set_id(data[0])

    return obj


def get_nb_rows(db):
    return db.get_nb_rows('SELECT COUNT(*) FROM RolePermission')


def get_all_rows(db):
    return db.get_all_rows('SELECT * FROM RolePermission')


class RolePermission:

    def __init__(self, role, permission):
        self.__id = None
        self.__role = role
        self.__permission = permission
        self.__message = ''

    # Getters
    def get_id(self):
        return self.__id

    def get_role(self):
        return self.__role

    def get_permission(self):
        return self.__permission

    def get_message(self):
        return self.__message

    # Setters
    def set_id(self, value):
        self.__id = value

    def set_role(self, value):
        self.__role = value

    def set_permission(self, value):
        self.__permission = value

    def set_message(self, value):
        self.__message = value

    # Methods
    def __append_message(self, value):
        self.__message += value

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

    def __validate_permission(self, db):
        permission = get_obj_permission(db, self.get_permission(), True)
        if self.get_permission() == '':
            self.__append_message("Permission cannot be empty.\n")
        elif permission is None:
            permission = get_obj_permission(db, self.get_permission())
            if permission is None:
                self.__append_message("Permission not exist.\n")
            else:
                self.set_permission(permission.get_id())

    def __exist(self, db):
        return get_obj(db, self.get_id(), True) is not None

    def __is_valid(self, db):
        self.set_message('')
        role_permission = get_obj(db, self.get_id(), True)
        if not role_permission.__exist(db) or (role_permission.__exist(db) and
                                               (role_permission.get_role() != self.get_role() or
                                                role_permission.get_permission() != self.get_permission())):
            self.__validate_role(db)
            self.__validate_permission(db)
            if self.__exist(db):
                self.__append_message(OBJET_NAME + " already exist.\n")

        if self.get_message() == '':
            self.set_message(OBJET_NAME + " valid.")
            return True

        return False

    def insert(self, db, user):
        if get_obj(db, [user.get_role, "Insert"]) is not None:
            if self.__is_valid(db):
                data = [
                    self.get_role(),
                    self.get_permission(),
                ]
                db.execute(
                    'INSERT INTO RolePermission VALUES (NULL, ?, ?, ?, current_timestamp, ?, current_timestamp)',
                    (data, user.get_id(), user.get_id(),)
                )
                self.set_message(OBJET_NAME + " inserted.")
        else:
            self.set_message("The user does not have permission to insert records into " + TABLE_NAME + " table.")

    def update(self, db, user):
        if get_obj(db, [user.get_role, "Update"]) is not None:
            if self.__is_valid(db):
                data = [
                    self.get_role(),
                    self.get_permission(),
                ]
                db.execute('''
                    UPDATE RolePermission SET 
                    RoleId = ?, PermissionId = ? , UpdateUserId = ?, UpdateDate = current_timestamp 
                    WHERE Id = ?
                ''', (data, user.get_id(), self.get_id(),))
                self.set_message(OBJET_NAME + " updated.")
        else:
            self.set_message("The user does not have permission to update records from " + TABLE_NAME + " table.")

    def delete(self, db, user):
        if get_obj(db, [user.get_role, "Delete"]) is not None:
            if self.__exist(db):
                db.execute('DELETE FROM RolePermission WHERE Id = ?', self.get_id())
                self.set_message(OBJET_NAME + " deleted.")
            else:
                self.set_message(OBJET_NAME + " not exist.")
        else:
            self.set_message("The user does not have permission to delete records from " + TABLE_NAME + " table.")

    def print(self, db):
        role = get_obj_role(db, self.get_role(), True)
        permission = get_obj_permission(db, self.get_permission(), True)

        print(OBJET_NAME.upper() + " DATA (" + self.get_id() + ")")
        print("Role: " + role.get_name())
        print("Permission: " + permission.get_name())
