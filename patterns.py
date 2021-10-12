from classes.Artist import get_name_list as get_artist_name_list, get_last_name_list as get_artist_last_name_list
from classes.Artwork import get_name_list as get_artwork_name_list
from classes.PlaceName import get_name_list as get_place_name_list

from dictionaries import search_in_dict


def search_in_patterns(db, nlp, keys, language):
    pattern_dict = {

        "English": {

            "move": [
                {"LOWER": {"IN": search_in_dict(db, ["move", "move"], language)}},
                {"POS": "PRON", "OP": "?"},
                {"POS": "DET", "OP": "?"},
                {"LOWER": {"IN": search_in_dict(db, ["move", "aux"], language)}, "OP": "?"},
                {"POS": "ADP", "OP": "?"},
                {"POS": "DET", "OP": "?"},
                {"LOWER": {"IN": get_place_name_list(db, language)}}
            ],

            "info_artist": [
                {"LOWER": {"IN": search_in_dict(db, ["info"], language)}},
                {"POS": "ADP", "OP": "?"},
                {"POS": "PRON", "OP": "?"},
                {"POS": "ADP", "OP": "?"},
                {"POS": "DET", "OP": "?"},
                {"LOWER": {"IN": get_artist_name_list(db, nlp)}, "OP": "*"},
                {"LOWER": {"IN": get_artist_last_name_list(db, nlp)}}
            ],

            "info_artwork": [
                {"LOWER": {"IN": search_in_dict(db, ["info"], language)}},
                {"POS": "ADP", "OP": "?"},
                {"POS": "PRON", "OP": "?"},
                {"POS": "ADP", "OP": "?"},
                {"POS": "DET", "OP": "?"},
                {"LOWER": {"IN": get_artwork_name_list(db, nlp)}}
            ],

            "show_map": [
                {"LOWER": {"IN": search_in_dict(db, ["show", "show"], language)}},
                {"POS": "PRON", "OP": "?"},
                {"POS": "DET", "OP": "?"},
                {"POS": "NOUN", "OP": "?"},
                {"LOWER": {"IN": search_in_dict(db, ["show", "map"], language)}}
            ],

            "greetings": [
                {"LOWER": {"IN": search_in_dict(db, ["greetings", "list"], language)}}
            ],

            "goodbye": [
                {"LOWER": {"IN": search_in_dict(db, ["goodbye", "list"], language)}}
            ],

            "name": [
                {"LOWER": {"IN": search_in_dict(db, ["name", "list1"], language)}},
                {"POS": "AUX"},
                {"POS": "PRON"},
                {"LOWER": {"IN": search_in_dict(db, ["name", "list2"], language)}}
            ],

            "utility": [
                {"LOWER": {"IN": search_in_dict(db, ["utility", "list1"], language)}},
                {"POS": "AUX", "OP": "?"},
                {"POS": "PRON", "OP": "?"},
                {"POS": "NOUN", "OP": "?"},
                {"LOWER": {"IN": search_in_dict(db, ["utility", "list2"], language)}}
            ],

            "enclosure_hours": [
                {"LOWER": {"IN": search_in_dict(db, ["enclosure_hours", "list1"], language)}},
                {"LOWER": {"IN": search_in_dict(db, ["enclosure_hours", "list2"], language)}}
            ],

            "location": [
                {"LOWER": {"IN": search_in_dict(db, ["location", "list1"], language)}},
                {"POS": "AUX", "OP": "?"},
                {"POS": "DET", "OP": "?"},
                {"LOWER": {"IN": search_in_dict(db, ["location", "list2"], language)}}
            ],

            "date": [
                {"LOWER": {"IN": search_in_dict(db, ["date", "list1"], language)}},
                {"LOWER": {"IN": search_in_dict(db, ["date", "list2"], language)}}
            ],

            "time": [
                {"LOWER": {"IN": search_in_dict(db, ["time", "list1"], language)}},
                {"LOWER": {"IN": search_in_dict(db, ["time", "list2"], language)}}
            ],

            "thanks": [
                {"LOWER": {"IN": search_in_dict(db, ["thanks", "list"], language)}}
            ],

            "login": [
                {"LOWER": {"IN": ["login", "login"]}}
            ],

            "logout": [
                {"LOWER": {"IN": ["log-out", "logout"]}}
            ],

            "show_row": [
                {"LOWER": {"IN": search_in_dict(db, ["show", "show"], language)}}
            ]
        },

        "Spanish": {

            "move": [
                {"LOWER": {"IN": search_in_dict(db, ["move", "move"], language)}},
                {"POS": "DET", "OP": "?"},
                {"LOWER": {"IN": search_in_dict(db, ["move", "aux"], language)}, "OP": "?"},
                {"POS": "ADP", "OP": "?"},
                {"POS": "DET", "OP": "?"},
                {"LOWER": {"IN": get_place_name_list(db, language)}}
            ],

            "info_artist": [
                {"LOWER": {"IN": search_in_dict(db, ["info"], language)}},
                {"POS": "ADP", "OP": "?"},
                {"POS": "DET", "OP": "?"},
                {"LOWER": {"IN": get_artist_name_list(db, nlp)}, "OP": "*"},
                {"LOWER": {"IN": get_artist_last_name_list(db, nlp)}}
            ],

            "info_artwork": [
                {"LOWER": {"IN": search_in_dict(db, ["info"], language)}},
                {"POS": "ADP", "OP": "?"},
                {"POS": "DET", "OP": "?"},
                {"LOWER": {"IN": get_artwork_name_list(db, nlp)}}
            ],

            "show_map": [
                {"LOWER": {"IN": search_in_dict(db, ["show", "show"], language)}},
                {"POS": "DET", "OP": "?"},
                {"LOWER": {"IN": search_in_dict(db, ["show", "map"], language)}}
            ],

            "greetings": [
                {"LOWER": {"IN": search_in_dict(db, ["greetings", "list"], language)}}
            ],

            "goodbye": [
                {"LOWER": {"IN": search_in_dict(db, ["goodbye", "list"], language)}}
            ],

            "name": [
                {"LOWER": {"IN": search_in_dict(db, ["name", "list1"], language)}},
                {"POS": "AUX", "OP": "?"},
                {"POS": "DET", "OP": "?"},
                {"POS": "PRON", "OP": "?"},
                {"LOWER": {"IN": search_in_dict(db, ["name", "list2"], language)}}
            ],

            "utility": [
                {"LOWER": {"IN": search_in_dict(db, ["utility", "list1"], language)}},
                {"LOWER": {"IN": search_in_dict(db, ["utility", "list2"], language)}}
            ],

            "enclosure_hours": [
                {"LOWER": {"IN": search_in_dict(db, ["enclosure_hours", "list1"], language)}},
                {"POS": "ADP", "OP": "?"},
                {"LOWER": {"IN": search_in_dict(db, ["enclosure_hours", "list2"], language)}}
            ],

            "location": [
                {"LOWER": {"IN": search_in_dict(db, ["location", "list1"], language)}},
                {"POS": "PRON", "OP": "?"},
                {"LOWER": {"IN": search_in_dict(db, ["location", "list2"], language)}, "OP": "?"},
                {"POS": "DET", "OP": "?"},
                {"LOWER": {"IN": search_in_dict(db, ["location", "list3"], language)}}
            ],

            "date": [
                {"LOWER": {"IN": search_in_dict(db, ["date", "list1"], language)}},
                {"LOWER": {"IN": search_in_dict(db, ["date", "list2"], language)}}
            ],

            "time": [
                {"LOWER": {"IN": search_in_dict(db, ["time", "list1"], language)}},
                {"LOWER": {"IN": search_in_dict(db, ["time", "list2"], language)}}
            ],

            "thanks": [
                {"LOWER": {"IN": search_in_dict(db, ["thanks", "list"], language)}}
            ],
        },

        "Portuguese": {

            "move": [
                {"LOWER": {"IN": search_in_dict(db, ["move", "move"], language)}},
                {"POS": "DET", "OP": "?"},
                {"LOWER": {"IN": search_in_dict(db, ["move", "aux"], language)}, "OP": "?"},
                {"POS": "ADP", "OP": "?"},
                {"POS": "DET", "OP": "?"},
                {"LOWER": {"IN": get_place_name_list(db, language)}}
            ],

            "info_artist": [
                {"LOWER": {"IN": search_in_dict(db, ["info"], language)}},
                {"POS": "ADP", "OP": "?"},
                {"POS": "DET", "OP": "?"},
                {"LOWER": {"IN": get_artist_name_list(db, nlp)}, "OP": "*"},
                {"LOWER": {"IN": get_artist_last_name_list(db, nlp)}}
            ],

            "info_artwork": [
                {"LOWER": {"IN": search_in_dict(db, ["info"], language)}},
                {"POS": "ADP", "OP": "?"},
                {"POS": "DET", "OP": "?"},
                {"LOWER": {"IN": get_artwork_name_list(db, nlp)}}
            ],

            "show_map": [
                {"LOWER": {"IN": search_in_dict(db, ["show", "show"], language)}},
                {"POS": "DET", "OP": "?"},
                {"LOWER": {"IN": search_in_dict(db, ["show", "map"], language)}}
            ],

            "greetings": [
                {"LOWER": {"IN": search_in_dict(db, ["greetings", "list"], language)}}
            ],

            "goodbye": [
                {"LOWER": {"IN": search_in_dict(db, ["goodbye", "list"], language)}}
            ],

            "name": [
                {"LOWER": {"IN": search_in_dict(db, ["name", "list1"], language)}},
                {"POS": "VERB", "OP": "?"},
                {"POS": "AUX", "OP": "?"},
                {"POS": "DET", "OP": "*"},
                {"LOWER": {"IN": search_in_dict(db, ["name", "list2"], language)}}
            ],

            "utility": [
                {"LOWER": {"IN": search_in_dict(db, ["utility", "list1"], language)}},
                {"POS": "PRON"},
                {"POS": "AUX", "OP": "?"},
                {"LOWER": {"IN": search_in_dict(db, ["utility", "list2"], language)}}
            ],

            "enclosure_hours": [
                {"LOWER": {"IN": search_in_dict(db, ["enclosure_hours", "list1"], language)}},
                {"POS": "ADP", "OP": "?"},
                {"LOWER": {"IN": search_in_dict(db, ["enclosure_hours", "list2"], language)}}
            ],

            "location": [
                {"LOWER": {"IN": search_in_dict(db, ["location", "list1"], language)}},
                {"POS": "PRON", "OP": "?"},
                {"POS": "DET", "OP": "?"},
                {"POS": "ADP", "OP": "?"},
                {"LOWER": {"IN": search_in_dict(db, ["location", "list2"], language)}}
            ],

            "date": [
                {"LOWER": {"IN": search_in_dict(db, ["date", "list1"], language)}},
                {"LOWER": {"IN": search_in_dict(db, ["date", "list2"], language)}}
            ],

            "time": [
                {"LOWER": {"IN": search_in_dict(db, ["time", "list1"], language)}},
                {"LOWER": {"IN": search_in_dict(db, ["time", "list2"], language)}}
            ],

            "thanks": [
                {"LOWER": {"IN": search_in_dict(db, ["thanks", "list"], language)}}
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
