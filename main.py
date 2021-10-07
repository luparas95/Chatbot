from classes.DatabaseManager import DatabaseManager
from classes.User import get_obj as get_obj_user
from classes.Language import select_language
from classes.Role import get_obj as get_obj_role

from spacy.matcher import Matcher
from time import sleep
from dictionaries import search_in_dict as srch_dict
from matcher import add, add_logged, login, move, info_artist, info_artwork, show_map, show_row


def main():

    db = DatabaseManager()
    user = get_obj_user(db, "public")

    language, nlp = select_language(db)
    matcher = add(db, nlp, Matcher(nlp.vocab), language.get_name())

    srch_dict(db, ["greeting"], language.get_name(), True)
    user_response = input()

    flag = True
    while flag:
        doc = nlp(user_response.lower())
        matches = matcher(doc)
        role = get_obj_role(db, user.get_role(), True)

        for match_id, start, end in matches:
            string_id = nlp.vocab.strings[match_id]

            if role.get_name() == "Public":
                if string_id == "login":
                    new_user = login(db)
                    if new_user is not None:
                        user = new_user
                        matcher = add_logged(db, nlp, Matcher(nlp.vocab))
                elif string_id == "move":
                    move(db, language.get_name())
                elif string_id == "info_artist":
                    info_artist(db, nlp, language, str(doc[end - 1]))
                elif string_id == "info_artwork":
                    info_artwork(db, nlp, language, str(doc[end - 1]))
                elif string_id == "show_map":
                    show_map(db, language.get_name())

            elif role.get_name() == "Administrator" or role.get_name() == "Super user":
                if string_id == "logout":
                    user = get_obj_user(db, "public")
                    matcher = add(db, nlp, Matcher(nlp.vocab), language.get_name())
                    print("Logout success.")
                elif string_id == "show_row":
                    if len(doc) > 3:
                        key = [str(doc[2]), str(doc[3])]
                    else:
                        key = str(doc[2])
                    show_row(db, str(doc[1]), key)

            sleep(1)

        if len(matches) == 0:
            srch_dict(db, ["not_understand"], language.get_name(), True)
        else:
            srch_dict(db, ["anything_else"], language.get_name(), True)

        user_response = input()

        if user_response == "end":
            flag = False

    db.close_conn()


if __name__ == "__main__":
    main()
