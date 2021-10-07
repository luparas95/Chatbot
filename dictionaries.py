from classes.Parameter import get_obj as get_obj_parameter


def search_in_dict(db, keys, language, is_ans=False):
    bot_name = get_obj_parameter(db, "bot name").get_value()
    opening_time = get_obj_parameter(db, "opening time").get_value()
    closing_time = get_obj_parameter(db, "closing time").get_value()
    address = get_obj_parameter(db, "address").get_value()

    dictionary = {

        "English": {

            "language": {
                "request": "Please indicate your language (en/es/pt):",
                "error": "The language is not valid, possible languages are en/es/pt. Try again: "
            },

            "greeting": "Hello! My name is " + bot_name + ". How can I help you?",

            "anything_else": "Can I help you with anything else?",

            "not_understand": "I'm sorry, I don't know what you mean. Can you repeat please?",

            "move": {
                "move": ["move", "go", "take", "drive", "lead", "direct", "show", "walk"],
                "aux": ["way", "rute"],
                "places": ["room", "hall", "wc"],
                "answer": "Very good, please follow me.",
            },

            "info": ["information", "info", "inform", "talk", "tell", "know"],

            "show": {
                "show": ["see", "show", "display", "print"],
                "map": ["map", "plane", "plat"],
                "answer": "This is the map of the enclosure.",
            },
        },


        "Spanish": {

            "greeting": "¡Hola! Mi nombre es " + bot_name + " ¿En que puedo ayudarte?",

            "anything_else": "¿Puedo ayudarle en algo más?",

            "not_understand": "Lo siento, no se a que se refiere. ¿Puede repetirlo por favor?",

            "move": {
                "move": [
                    "ir", "llevar", "llévame", "llévanos", "conducir", "condúceme", "condúcenos",
                    "dirigir", "dirégeme", "dirígete", "dirígenos", "mostrar", "muéstrame", "muéstranos",
                    "muévete", "desplázate", "camina"
                ],
                "aux": ["camino", "ruta"],
                "places": ["entrada", "pasillo", "sala-1", "servicio", "wc"],
                "answer": "Muy bien, por favor sigame.",
            },

            "info": [
                "información", "info", "informar", "informame", "informanos", "hablar", "hablame", "hablanos", "contar",
                "cuentame", "cuentanos", "decir", "decirme", "decirnos", "saber", "sabes", "conocer", "conoces"
            ],

            "show": {
                "show": ["ver", "desplegar", "mostrar", "muestrame", "muestranos", "enseñar", "enséñame", "enséñanos"],
                "map": ["mapa", "plano"],
                "answer": "Este es el mapa del recinto.",
            },
        },


        "Portuguese": {

            "greeting": "Olá! Meu nome é " + bot_name + ". Como posso ajudá-lo?",

            "anything_else": "Posso te ajudar com mais alguma coisa?",

            "not_understand": "Desculpa nao sei o que queres dizer. Você pode repetir por favor?",

            "move": {
                "move": [
                    "vá", "vai", "leve-me", "leve-nos", "direcione-me", "direcione-nos", "mostre-me", "mostre-nos",
                    "role", "caminhe",
                ],
                "aux": ["caminho", "estrada", "rua", "rota"],
                "places": ["quarto", "corredor", "entrada", "wc"],
                "answer": "Muito bom, por favor me siga.",
            },

            "info": [
                "informação", "info", "informe", "informe-me", "informe-nos", "fale", "diga", "diga-me", "diga-nos",
                "conheça"
            ],

            "show": {
                "show": [
                    "ver", "revelar", "mostrar", "mostrar-me", "mostrar-nos", "ensinar", "mostrar-me", "mostrar-nos"
                ],
                "map": ["mapa", "plano"],
                "answer": "Este é o mapa do recinto.",
            },
        },
    }

    if language in list(dictionary):
        res = dictionary[language]

        for key in keys:

            if key in list(res):
                res = res[key]

            else:
                res = None
                print("Key (" + key + ") not found in " + language + " dictionary.")
                break

    else:
        res = None
        print("Language (" + language + ") not found in dictionary.")

    if is_ans:
        print(bot_name + ": " + res)
        return None

    else:
        return res
