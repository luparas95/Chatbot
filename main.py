from classes.DatabaseManager import DatabaseManager
from classes.User import get_obj as get_obj_user
from classes.Language import select_language
from classes.Parameter import get_obj as get_obj_parameter
from classes.Artist import srch_by_last_name as srch_artist_by_last_name
from classes.ArtistInfo import get_obj as get_obj_artist_info
from classes.Artwork import srch_by_name as srch_artwork_by_name
from classes.ArtworkInfo import get_obj as get_obj_artwork_info

from spacy.matcher import Matcher
import cv2
from os import path, getcwd
from time import sleep
from dictionaries import search_in_dict as srch_dict
from matcher import matcher_add


def main():

    db = DatabaseManager()
    user = get_obj_user(db, "public")
    bot_name = get_obj_parameter(db, "bot name").get_value()

    language, nlp = select_language(db)

    srch_dict(db, ["greeting"], language.get_name(), True)

    matcher = matcher_add(db, nlp, Matcher(nlp.vocab), language.get_name())

    flag = True
    while flag:
        user_response = input()
        doc = nlp(user_response.lower())
        matches = matcher(doc)

        sleep(1)

        for match_id, start, end in matches:

            string_id = nlp.vocab.strings[match_id]

            if string_id == "move":
                srch_dict(db, ["move", "answer"], language.get_name(), True)

            elif string_id == "info_artist":
                artist = srch_artist_by_last_name(db, nlp, str(doc[end - 1]))
                artist_info = get_obj_artist_info(db, [artist.get_id(), language.get_id()])
                print(bot_name + ": " + artist_info.get_description())

            elif string_id == "info_artwork":
                artwork = srch_artwork_by_name(db, nlp, str(doc[end - 1]))
                artwork_info = get_obj_artwork_info(db, [artwork.get_id(), language.get_id()])
                print(bot_name + ": " + artwork_info.get_description())

            elif string_id == "show":
                img = cv2.imread(path.join(getcwd(), get_obj_parameter(db, "img mape path").get_value()))

                if img is None:
                    print("There was an error loading the image.")

                else:
                    srch_dict(db, ["show", "answer"], language.get_name(), True)

                    width = get_obj_parameter(db, "img mape width").get_value()
                    height = get_obj_parameter(db, "img mape height").get_value()

                    img_size = (int(width), int(height))
                    resize_img = cv2.resize(img, img_size)

                    cv2.imshow(srch_dict(db, ["show", "map"], language.get_name())[0], resize_img)
                    cv2.waitKey()
                    cv2.destroyAllWindows()

            sleep(1)

        if len(matches) == 0:
            srch_dict(db, ["not_understand"], language.get_name(), True)

        for match_id, start, end in matches:
            print("Resultado encontrado:", doc[start:end].text)

        for token in doc:
            token_text = token.text
            token_pos = token.pos_
            token_dep = token.dep_

            print("{:<12}{:<10}{:<10}".format(token_text, token_pos, token_dep))

        if user_response == "end":
            flag = False

    db.close_conn()


if __name__ == "__main__":
    main()
