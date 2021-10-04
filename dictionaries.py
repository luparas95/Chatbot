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

            "not_understand": "I'm sorry, I don't know what you mean.",

            "move": {
                "move": ["move", "go", "take", "drive", "lead", "direct", "show", "walk"],
                "aux": ["way", "rute"],
                "places": ["room", "hall", "wc"],
                "answer": "Very good, please follow me.",
            },

            "info": ["information", "info", "inform", "talk", "tell", "know"],

            "show": {
                "show": ["see", "show", "display"],
                "map": ["map", "plane", "plat"],
                "answer": "This is the map of the enclosure.",
            },

            "training": {
                "greetings": {
                    "patterns": ["hello", "hey", "hi", "greetings", "what's up", "how is it going", "good day"],
                    "answers": ["Hey!", "Hello!", "Hi, it's a pleasure talking to you."]
                },
                "goodbye": {
                    "patterns": ["bye", "goodbye", "see you later", "have a good day", "i am leaving", "see ya"],
                    "answers": ["Goodbye!", "Bye, I hope have been useful.", "See you soon!"]
                },
                "name": {
                    "patterns": ["what is your name", "what should i call you", "how can i call you"],
                    "answers": [
                        "My name is " + bot_name + ".", "You can call me" + bot_name + ".",
                        "I'm " + bot_name + "."
                    ]
                },
                "be": {
                    "patterns": ["what are you", "who are you"],
                    "answers": ["I am " + bot_name + ", an assistant robot."]
                },
                "utility": {
                    "patterns": ["what are you for", "what do you know do", "what use do you have"],
                    "answers": [
                        "I can do many things, such as guide you around the venue or give you information about works "
                        "and authors."
                    ]
                },
                "horario": {
                    "patterns": [],
                    "answers": []
                },
                "where": {
                    "patterns": [],
                    "answers": []
                },
                "thanks": {
                    "patterns": [],
                    "answers": []
                },
            },
        },


        "Spanish": {

            "greeting": "¡Hola! Mi nombre es " + bot_name + " ¿En que puedo ayudarte?",

            "not_understand": "Lo siento, no se a que se refiere.",

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

            "training": {
                "greetings": {
                    "patterns": ["hola", "hey", "saludos", "buenas", "buenos días", "buenas tardes"],
                    "answers": ["¡Muy buenas!", "¡Hola!", "Hola es un placer hablar contigo"]
                },
                "goodbye": {
                    "patterns": ["adios", "hasta luego", "nos vemos", "ten un buen día", "me voy", "chao"],
                    "answers": ["Adios!", "Adios, espero haberte sido de utilidad.", "Hasta pronto!"]
                },
                "name": {
                    "patterns": ["cual es tu nombre", "como te llamas", "como puedo llamarte"],
                    "answers": [
                        "Mi nombre es " + bot_name + ".", "Puedes llamarme " + bot_name + ".",
                        "Soy " + bot_name + "."
                    ]
                },
                "be": {
                    "patterns": ["que eres", "que es lo que eres", "quien eres"],
                    "answers": ["Soy " + bot_name + ", un robot de servicio."]
                },
                "utility": {
                    "patterns": ["para que sirves", "que sabes hacer", "que usos tienes"],
                    "answers": [
                        "Puedo hacer muchas cosas, como guiarte por el recinto o darte información sobre obras y "
                        "autores."
                    ]
                },
                "horario": {
                    "patterns": ["horario del museo", "hora de cierre", "horario de apertura"],
                    "answers": [
                        "El horario del museo es de " + opening_time + " a " + closing_time + "."
                    ]
                },
                "where": {
                    "patterns": ["dirección del museo", "donde se encuentra el museo", "en que calle esta el museo"],
                    "answers": ["La dirección del recinto es: " + address]
                },
                "thanks": {
                    "patterns": ["gracias", "agradecido"],
                    "answers": ["De nada, ¡Es un placer poder ayudarte!"]
                },
            },
        },


        "Portuguese": {

            "greeting": "Olá! Meu nome é " + bot_name + ". Como posso ajudá-lo?",

            "not_understand": "Desculpa nao sei o que queres dizer.",

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

            "training": {
                "greetings": {
                    "patterns": ["hello", "hey", "hi", "greetings", "what's up", "how is it going", "good day"],
                    "answers": ["Hey!", "Hello!", "What can I do for you?"]
                },
                "goodbye": {
                    "patterns": ["bye", "goodbye", "see you later", "have a good day", "i am leaving", "see ya"],
                    "answers": ["Goodbye!", "Bye, I hope have been useful.", "See you soon!"]
                },
                "name": {
                    "patterns": ["what is your name", "what should i call you", "who are you", "how can i call you"],
                    "answers": [
                        "My name is " + bot_name + ".", "You can call me" + bot_name + ".",
                        "I'm " + bot_name + "."
                    ]
                },
                "be": {
                    "patterns": ["what are you"],
                    "answers": ["I am an assistant robot"]
                },
                "utility": {
                    "patterns": ["what are you for", "what do you know do", "what use do you have"],
                    "answers": [
                        "I can do many things, such as guide you around the venue or give you information about works "
                        "and authors"
                    ]
                },
                "horario": {
                    "patterns": [],
                    "answers": []
                },
                "where": {
                    "patterns": [],
                    "answers": []
                },
                "thanks": {
                    "patterns": [],
                    "answers": []
                },
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
