from classes.Artist import get_obj as get_obj_artist
from classes.ArtistInfo import get_obj as get_obj_artist_info
from classes.Artwork import get_obj as get_obj_artwork
from classes.ArtworkInfo import get_obj as get_obj_artwork_info
from classes.Parameter import get_obj as get_obj_parameter
from classes.User import get_obj as get_obj_user
from classes.Language import get_obj as get_obj_language
from classes.Nationality import get_obj as get_obj_nationality
from classes.Permission import get_obj as get_obj_permission
from classes.Role import get_obj as get_obj_role
from classes.RolePermission import get_obj as get_obj_role_permission
from classes.Place import get_obj as get_obj_place
from classes.PlaceName import get_obj as get_obj_place_name

from patterns import search_in_patterns as srch_patt
from dictionaries import search_in_dict as srch_dict
import cv2
from os import path, getcwd
from werkzeug.security import check_password_hash
from random import randint


def add(db, nlp, matcher, language):
    matcher.add("move", [srch_patt(db, nlp, ["move"], language)])
    matcher.add("info_artist", [srch_patt(db, nlp, ["info_artist"], language)])
    matcher.add("info_artwork", [srch_patt(db, nlp, ["info_artwork"], language)])
    matcher.add("show_map", [srch_patt(db, nlp, ["show_map"], language)])
    matcher.add("greetings", [srch_patt(db, nlp, ["greetings"], language)])
    matcher.add("goodbye", [srch_patt(db, nlp, ["goodbye"], language)])
    matcher.add("name", [srch_patt(db, nlp, ["name"], language)])
    matcher.add("utility", [srch_patt(db, nlp, ["utility"], language)])
    matcher.add("enclosure_hours", [srch_patt(db, nlp, ["enclosure_hours"], language)])
    matcher.add("location", [srch_patt(db, nlp, ["location"], language)])
    matcher.add("date", [srch_patt(db, nlp, ["date"], language)])
    matcher.add("time", [srch_patt(db, nlp, ["time"], language)])
    matcher.add("thanks", [srch_patt(db, nlp, ["thanks"], language)])

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


def move(db, language, place_name_name):
    bot_name = get_obj_parameter(db, "bot name").get_value()

    place_name = get_obj_place_name(db, [language.get_id(), place_name_name])
    place = get_obj_place(db, place_name.get_place(), True)

    srch_dict(db, ["move", "answer"], language.get_name(), True)
    print(bot_name + ": Coodinates (" + str(place.get_x_coordinate()) + ", " + str(place.get_y_coordinate()) + ")")


def info_artist(db, language, artist_last_name):
    bot_name = get_obj_parameter(db, "bot name").get_value()

    artist = get_obj_artist(db, artist_last_name)
    artist_info = get_obj_artist_info(db, [artist.get_id(), language.get_id()])

    print(bot_name + ": " + artist_info.get_name())


def info_artwork(db, language, artwork_name):
    bot_name = get_obj_parameter(db, "bot name").get_value()

    artwork = get_obj_artwork(db, artwork_name)
    artwork_info = get_obj_artwork_info(db, [artwork.get_id(), language.get_id()])

    print(bot_name + ": " + artwork_info.get_name())


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


def greetings(db, language):
    bot_name = get_obj_parameter(db, "bot name").get_value()

    answers = srch_dict(db, ["greetings", "answer"], language)
    n_random = randint(0, len(answers) - 1)

    print(bot_name + ": " + answers[n_random])


def goodbye(db, language):
    bot_name = get_obj_parameter(db, "bot name").get_value()

    answers = srch_dict(db, ["goodbye", "answer"], language)
    n_random = randint(0, len(answers) - 1)

    print(bot_name + ": " + answers[n_random])


def name(db, language):
    bot_name = get_obj_parameter(db, "bot name").get_value()

    answers = srch_dict(db, ["name", "answer"], language)
    n_random = randint(0, len(answers) - 1)

    print(bot_name + ": " + answers[n_random])


def utility(db, language):
    srch_dict(db, ["utility", "answer"], language, True)


def enclosure_hours(db, language):
    srch_dict(db, ["enclosure_hours", "answer"], language, True)


def location(db, language):
    srch_dict(db, ["location", "answer"], language, True)


def date(db, language):
    srch_dict(db, ["date", "answer"], language, True)


def time(db, language):
    srch_dict(db, ["time", "answer"], language, True)


def thanks(db, language):
    srch_dict(db, ["thanks", "answer"], language, True)


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

    elif table_name == "place":
        obj = get_obj_place(db, key)
        if obj is None:
            obj = get_obj_place(db, int(key), True)
        if obj is not None:
            obj.print()

    elif table_name == "placename":
        obj = get_obj_place_name(db, key)
        if obj is None:
            obj = get_obj_place_name(db, int(key), True)
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
