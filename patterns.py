from classes.Artist import get_name_list as get_artist_name_list, get_last_name_list as get_artist_last_name_list
from classes.Artwork import get_name_list as get_artwork_name_list

from dictionaries import search_in_dict


def search_in_patterns(db, nlp, keys, language):
    pattern_dict = {

        "English": {

            "move": [
                {"LOWER": {"IN": search_in_dict(db, ["move", "move"], "English")}},
                {"POS": "PRON", "OP": "?"},
                {"POS": "DET", "OP": "?"},
                {"LOWER": {"IN": search_in_dict(db, ["move", "aux"], "English")}, "OP": "?"},
                {"POS": "ADP", "OP": "?"},
                {"POS": "DET", "OP": "?"},
                {"LOWER": {"IN": search_in_dict(db, ["move", "places"], "English")}}
            ],

            "info_artist": [
                {"LOWER": {"IN": search_in_dict(db, ["info"], "English")}},
                {"POS": "ADP", "OP": "?"},
                {"POS": "PRON", "OP": "?"},
                {"POS": "ADP", "OP": "?"},
                {"POS": "DET", "OP": "?"},
                {"LOWER": {"IN": get_artist_name_list(db, nlp)}, "OP": "*"},
                {"LOWER": {"IN": get_artist_last_name_list(db, nlp)}}
            ],

            "info_artwork": [
                {"LOWER": {"IN": search_in_dict(db, ["info"], "English")}},
                {"POS": "ADP", "OP": "?"},
                {"POS": "PRON", "OP": "?"},
                {"POS": "ADP", "OP": "?"},
                {"POS": "DET", "OP": "?"},
                {"LOWER": {"IN": get_artwork_name_list(db, nlp)}}
            ],

            "show_map": [
                {"LOWER": {"IN": search_in_dict(db, ["show", "show"], "English")}},
                {"POS": "PRON", "OP": "?"},
                {"POS": "DET", "OP": "?"},
                {"POS": "NOUN", "OP": "?"},
                {"LOWER": {"IN": search_in_dict(db, ["show", "map"], "English")}}
            ],

            "login": [
                {"LOWER": {"IN": ["login", "login"]}}
            ],

            "logout": [
                {"LOWER": {"IN": ["log-out", "logout"]}}
            ],

            "show_row": [
                {"LOWER": {"IN": search_in_dict(db, ["show", "show"], "English")}}
            ]
        },

        "Spanish": {

            "move": [
                {"LOWER": {"IN": search_in_dict(db, ["move", "move"], "Spanish")}},
                {"POS": "DET", "OP": "?"},
                {"LOWER": {"IN": search_in_dict(db, ["move", "aux"], "Spanish")}, "OP": "?"},
                {"POS": "ADP", "OP": "?"},
                {"POS": "DET", "OP": "?"},
                {"LOWER": {"IN": search_in_dict(db, ["move", "places"], "Spanish")}}
            ],

            "info_artist": [
                {"LOWER": {"IN": search_in_dict(db, ["info"], "Spanish")}},
                {"POS": "ADP", "OP": "?"},
                {"POS": "DET", "OP": "?"},
                {"LOWER": {"IN": get_artist_name_list(db, nlp)}, "OP": "*"},
                {"LOWER": {"IN": get_artist_last_name_list(db, nlp)}}
            ],

            "info_artwork": [
                {"LOWER": {"IN": search_in_dict(db, ["info"], "Spanish")}},
                {"POS": "ADP", "OP": "?"},
                {"POS": "DET", "OP": "?"},
                {"LOWER": {"IN": get_artwork_name_list(db, nlp)}}
            ],

            "show_map": [
                {"LOWER": {"IN": search_in_dict(db, ["show", "show"], "Spanish")}},
                {"POS": "DET", "OP": "?"},
                {"LOWER": {"IN": search_in_dict(db, ["show", "map"], "Spanish")}}
            ],
        },

        "Portuguese": {

            "move": [
                {"LOWER": {"IN": search_in_dict(db, ["move", "move"], "Portuguese")}},
                {"POS": "DET", "OP": "?"},
                {"LOWER": {"IN": search_in_dict(db, ["move", "aux"], "Portuguese")}, "OP": "?"},
                {"POS": "ADP", "OP": "?"},
                {"POS": "DET", "OP": "?"},
                {"LOWER": {"IN": search_in_dict(db, ["move", "places"], "Portuguese")}}
            ],

            "info_artist": [
                {"LOWER": {"IN": search_in_dict(db, ["info"], "Portuguese")}},
                {"POS": "ADP", "OP": "?"},
                {"POS": "DET", "OP": "?"},
                {"LOWER": {"IN": get_artist_name_list(db, nlp)}, "OP": "*"},
                {"LOWER": {"IN": get_artist_last_name_list(db, nlp)}}
            ],

            "info_artwork": [
                {"LOWER": {"IN": search_in_dict(db, ["info"], "Portuguese")}},
                {"POS": "ADP", "OP": "?"},
                {"POS": "DET", "OP": "?"},
                {"LOWER": {"IN": get_artwork_name_list(db, nlp)}}
            ],

            "show_map": [
                {"LOWER": {"IN": search_in_dict(db, ["show", "show"], "Portuguese")}},
                {"POS": "DET", "OP": "?"},
                {"LOWER": {"IN": search_in_dict(db, ["show", "map"], "Portuguese")}}
            ],
        },
    }

    if language in list(pattern_dict):
        res = pattern_dict[language]

        for key in keys:

            if key in list(res):
                res = res[key]

            else:
                res = None
                print("Key (" + key + ") not found in " + language + " patterns.")
                break

    else:
        res = None
        print("Language (" + language + ") not found in patterns.")

    return res
