from classes.RolePermission import get_obj as get_obj_role_permission

OBJECT_NAME = "Place"
TABLE_NAME = "Place"
FIELD_MAX_SIZE = {
    "XCoordinate": 200,
    "YCoordinate": 200,
}


def get_obj(db, value, by_id=False):
    if by_id:
        data = db.execute(1, 'SELECT * FROM Place WHERE Id = ?', (value,))
    else:
        data = db.execute(1, 'SELECT * FROM Place WHERE XCoordinate = ? AND YCoordinate = ?', (value[0], value[1]))

    if data is None:
        return None

    obj = Place(
        data[1],
        data[2],
    )
    obj.set_id(data[0])

    return obj


def get_nb_rows(db):
    return db.execute(1, 'SELECT COUNT(*) FROM Place')


def get_all_rows(db):
    return db.execute(2, 'SELECT * FROM Place')


class Place:

    def __init__(self, x_coordinate, y_coordinate):
        self.__id = None
        self.__x_coordinate = x_coordinate
        self.__y_coordinate = y_coordinate
        self.__message = ''

    # Getters
    def get_id(self):
        return self.__id

    def get_x_coordinate(self):
        return self.__x_coordinate

    def get_y_coordinate(self):
        return self.__y_coordinate

    def get_message(self):
        return self.__message

    # Setters
    def set_id(self, value):
        self.__id = value

    def set_x_coordinate(self, value):
        self.__x_coordinate = value

    def set_y_coordinate(self, value):
        self.__y_coordinate = value

    def set_message(self, value):
        self.__message = value

    # Methods
    def __append_message(self, value):
        self.__message += value

    def __validate_x_coordinate(self):
        if self.get_x_coordinate() == '':
            self.__append_message("XCoordinate cannot be empty.\n")
        elif len(self.get_x_coordinate()) < 0:
            self.__append_message("XCoordinate cannot be less than 0.\n")
        elif len(self.get_x_coordinate()) > FIELD_MAX_SIZE["XCoordinate"]:
            self.__append_message("XCoordinate cannot be greater than " + str(FIELD_MAX_SIZE["XCoordinate"]) + ".\n")

    def __validate_y_coordinate(self):
        if self.get_y_coordinate() == '':
            self.__append_message("YCoordinate cannot be empty.\n")
        elif len(self.get_y_coordinate()) < 0:
            self.__append_message("YCoordinate cannot be less than 0.\n")
        elif len(self.get_y_coordinate()) > FIELD_MAX_SIZE["YCoordinate"]:
            self.__append_message("YCoordinate cannot be greater than " + str(FIELD_MAX_SIZE["YCoordinate"]) + ".\n")

    def __exist(self, db):
        return get_obj(db, self.get_id(), True) is not None

    def __is_valid(self, db):
        self.set_message('')
        place = get_obj(db, self.get_id(), True)
        if not place.__exist(db) or (place.__exist(db) and place.get_x_coordinate() != self.get_x_coordinate()) \
                or (place.__exist(db) and place.get_y_coordinate() != self.get_y_coordinate()):
            self.__validate_x_coordinate()
            self.__validate_y_coordinate()
            if get_obj(db, (self.get_x_coordinate(), self.get_y_coordinate())) is not None:
                self.__append_message(OBJECT_NAME + " already exist.\n")

        if self.get_message() == '':
            self.set_message(OBJECT_NAME + " valid.")
            return True

        return False

    def insert(self, db, user):
        if get_obj_role_permission([user.get_role, "Insert"], db) is not None:
            if self.__is_valid(db):
                data = [
                    self.get_x_coordinate(),
                    self.get_y_coordinate(),
                ]
                db.execute(
                    3, 'INSERT INTO Place VALUES (NULL, ?, ?, ?, current_timestamp, ?, current_timestamp)',
                    (data, user.get_id(), user.get_id(),)
                )
                self.set_message(OBJECT_NAME + " inserted.")
        else:
            self.set_message("The user does not have permission to insert records into " + TABLE_NAME + " table.")

    def update(self, db, user):
        if get_obj_role_permission([user.get_role, "Update"], db) is not None:
            if self.__is_valid(db):
                data = [
                    self.get_x_coordinate(),
                    self.get_y_coordinate(),
                ]
                db.execute(
                    3, '''
                    UPDATE Place SET 
                    XCoordinate = ?, YCoordinate = ?, UpdateUserId = ?, 
                    UpdateDate = current_timestamp 
                    WHERE Id = ?
                    ''', (data, user.get_id(), self.get_id(),)
                )
                self.set_message(OBJECT_NAME + " updated.")
        else:
            self.set_message("The user does not have permission to update records from " + TABLE_NAME + " table.")

    def delete(self, db, user):
        if get_obj_role_permission(db, [user.get_role, "Delete"]) is not None:
            if self.__exist(db):
                db.execute(3, 'DELETE FROM Place WHERE Id = ?', self.get_id())
                self.set_message(OBJECT_NAME + " deleted.")
            else:
                self.set_message(OBJECT_NAME + " not exist.")
        else:
            self.set_message("The user does not have permission to delete records from " + TABLE_NAME + " table.")

    def print(self):
        print(OBJECT_NAME.upper() + " DATA (" + str(self.get_id()) + ")")
        print("X coordinate: " + self.get_x_coordinate())
        print("Y coordinate: " + self.get_y_coordinate())
