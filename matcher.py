from classes.Artist import srch_by_last_name as srch_artist_by_last_name, get_obj as get_obj_artist
from classes.ArtistInfo import get_obj as get_obj_artist_info
from classes.Artwork import srch_by_name as srch_artwork_by_name, get_obj as get_obj_artwork
from classes.ArtworkInfo import get_obj as get_obj_artwork_info
from classes.Parameter import get_obj as get_obj_parameter
from classes.User import get_obj as get_obj_user
from classes.Language import get_obj as get_obj_language
from classes.Nationality import get_obj as get_obj_nationality
from classes.Permission import get_obj as get_obj_permission
from classes.Role import get_obj as get_obj_role
from classes.RolePermission import get_obj as get_obj_role_permission

from patterns import search_in_patterns as srch_patt
from dictionaries import search_in_dict as srch_dict
import cv2
from os import path, getcwd
from werkzeug.security import check_password_hash


def add(db, nlp, matcher, language):
    matcher.add("move", [srch_patt(db, nlp, ["move"], language)])
    matcher.add("info_artist", [srch_patt(db, nlp, ["info_artist"], language)])
    matcher.add("info_artwork", [srch_patt(db, nlp, ["info_artwork"], language)])
    matcher.add("show_map", [srch_patt(db, nlp, ["show_map"], language)])

    if language == "English":
        matcher.add("login", [srch_patt(db, nlp, ["login"], language)])

    return matcher


def add_logged(db, nlp, matcher):
    matcher.add("logout", [srch_patt(db, nlp, ["logout"], "English")])
    matcher.add("show_row", [srch_patt(db, nlp, ["show_row"], "English")])

    return matcher


def login(db):
    print("Enter user's nickname: ")
    nick = input()

    user = get_obj_user(db, nick)

    if user is not None:
        print("Enter user's password: ")
        password = input()
        if check_password_hash(user.get_password(), password):
            print("Login success.")
            return user
        else:
            print("User's password does not exist.")
    else:
        print("User's nickname does not exist.")

    return None


def move(db, language):
    srch_dict(db, ["move", "answer"], language, True)


def info_artist(db, nlp, language, artist_last_name):
    bot_name = get_obj_parameter(db, "bot name").get_value()

    artist = srch_artist_by_last_name(db, nlp, artist_last_name)
    artist_info = get_obj_artist_info(db, [artist.get_id(), language.get_id()])

    print(bot_name + ": " + artist_info.get_description())


def info_artwork(db, nlp, language, artwork_name):
    bot_name = get_obj_parameter(db, "bot name").get_value()

    artwork = srch_artwork_by_name(db, nlp, artwork_name)
    artwork_info = get_obj_artwork_info(db, [artwork.get_id(), language.get_id()])

    print(bot_name + ": " + artwork_info.get_description())


def show_map(db, language):
    img = cv2.imread(path.join(getcwd(), get_obj_parameter(db, "img mape path").get_value()))

    if img is None:
        print("There was an error loading the image.")

    else:
        srch_dict(db, ["show", "answer"], language, True)

        width = get_obj_parameter(db, "img mape width").get_value()
        height = get_obj_parameter(db, "img mape height").get_value()

        img_size = (int(width), int(height))
        resize_img = cv2.resize(img, img_size)

        cv2.imshow(srch_dict(db, ["show", "map"], language)[0], resize_img)
        cv2.waitKey()
        cv2.destroyAllWindows()


def show_row(db, table_name, key):
    obj = None
    if table_name == "artist":
        obj = get_obj_artist(db, key)
        if obj is None:
            obj = get_obj_artist(db, int(key), True)
        if obj is not None:
            obj.print(db)

    elif table_name == "artistinfo":
        obj = get_obj_artist_info(db, key)
        if obj is None:
            obj = get_obj_artist_info(db, int(key), True)
        if obj is not None:
            obj.print(db)

    elif table_name == "artwork":
        obj = get_obj_artwork(db, key)
        if obj is None:
            obj = get_obj_artwork_info(db, int(key), True)
        if obj is not None:
            obj.print(db)

    elif table_name == "artworkinfo":
        obj = get_obj_artwork_info(db, key)
        if obj is None:
            obj = get_obj_artwork_info(db, int(key), True)
        if obj is not None:
            obj.print(db)

    elif table_name == "language":
        obj = get_obj_language(db, key)
        if obj is None:
            obj = get_obj_language(db, int(key), True)
        if obj is not None:
            obj.print()

    elif table_name == "nationality":
        obj = get_obj_nationality(db, key)
        if obj is None:
            obj = get_obj_nationality(db, int(key), True)
        if obj is not None:
            obj.print()

    elif table_name == "parameter":
        obj = get_obj_parameter(db, key)
        if obj is None:
            obj = get_obj_parameter(db, int(key), True)
        if obj is not None:
            obj.print()

    elif table_name == "permission":
        obj = get_obj_permission(db, key)
        if obj is None:
            obj = get_obj_permission(db, int(key), True)
        if obj is not None:
            obj.print()

    elif table_name == "role":
        obj = get_obj_role(db, key)
        if obj is None:
            obj = get_obj_role(db, key, int(key))
        if obj is not None:
            obj.print()

    elif table_name == "rolepermission":
        obj = get_obj_role_permission(db, key)
        if obj is None:
            obj = get_obj_role_permission(db, int(key), True)
        if obj is not None:
            obj.print(db)

    elif table_name == "user":
        obj = get_obj_user(db, key)
        if obj is None:
            obj = get_obj_user(db, int(key), True)
        if obj is not None:
            obj.print(db)

    else:
        print(table_name + " table not found.")

    if obj is None:
        print("Key '" + key + "' not found in " + table_name + " table.")
