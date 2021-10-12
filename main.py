from classes.DatabaseManager import DatabaseManager
from classes.User import get_obj as get_obj_user
from classes.Language import select_language
from classes.Role import get_obj as get_obj_role

from spacy.matcher import Matcher
from time import sleep
from dictionaries import search_in_dict as srch_dict
import matcher as match


def main():

    db = DatabaseManager()
    user = get_obj_user(db, "public")

    language, nlp = select_language(db)
    matcher = match.add(db, nlp, Matcher(nlp.vocab), language.get_name())

    srch_dict(db, ["greetings", "intro"], language.get_name(), True)
    user_response = input()

    run = True
    while run:
        doc = nlp(user_response.lower())
        matches = matcher(doc)
        role = get_obj_role(db, user.get_role(), True)

        for match_id, start, end in matches:
            string_id = nlp.vocab.strings[match_id]

            if role.get_name() == "Public":
                if string_id == "login":
                    new_user = match.login(db)
                    if new_user is not None:
                        user = new_user
                        matcher = match.add_logged(db, nlp, Matcher(nlp.vocab))
                elif string_id == "move":
                    match.move(db, language, str(doc[end - 1]).capitalize())
                elif string_id == "info_artist":
                    match.info_artist(db, language, str(doc[end - 1]).capitalize())
                elif string_id == "info_artwork":
                    match.info_artwork(db, language, str(doc[end - 1]).capitalize())
                elif string_id == "show_map":
                    match.show_map(db, language.get_name())
                elif string_id == "greetings":
                    match.greetings(db, language.get_name())
                elif string_id == "goodbye":
                    match.goodbye(db, language.get_name())
                    run = False
                elif string_id == "name":
                    match.name(db, language.get_name())
                elif string_id == "utility":
                    match.utility(db, language.get_name())
                elif string_id == "enclosure_hours":
                    match.enclosure_hours(db, language.get_name())
                elif string_id == "location":
                    match.location(db, language.get_name())
                elif string_id == "date":
                    match.date(db, language.get_name())
                elif string_id == "time":
                    match.time(db, language.get_name())
                elif string_id == "thanks":
                    match.thanks(db, language.get_name())

            elif role.get_name() == "Administrator" or role.get_name() == "Super user":
                if string_id == "logout":
                    user = get_obj_user(db, "public")
                    matcher = match.add(db, nlp, Matcher(nlp.vocab), language.get_name())
                    print("Logout success.")
                elif string_id == "show_row":
                    if len(doc) > 3:
                        key = [str(doc[2]), str(doc[3])]
                    else:
                        key = str(doc[2])
                    match.show_row(db, str(doc[1]), key)

            sleep(1)

        if len(matches) == 0:
            srch_dict(db, ["not_understand"], language.get_name(), True)

        if run:
            user_response = input()

    db.get_db().close()


if __name__ == "__main__":
    main()
