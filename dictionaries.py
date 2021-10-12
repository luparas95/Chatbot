from classes.Parameter import get_obj as get_obj_parameter

from datetime import datetime


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

            "not_understand": "I'm sorry, I don't know what you mean. Can you repeat please?",

            "move": {
                "move": ["move", "go", "take", "drive", "lead", "direct", "show", "walk"],
                "aux": ["way", "rute"],
                "answer": "Very good, please follow me.",
            },

            "info": ["information", "info", "inform", "talk", "tell", "know"],

            "show": {
                "show": ["see", "show", "display", "print"],
                "map": ["map", "plane", "plat"],
                "answer": "This is the map of the enclosure.",
            },

            "greetings": {
                "intro": "Hello! My name is " + bot_name + ". How can I help you?",
                "list": ["hello", "hey", "hi", "greetings"],
                "answer": ["Hey!", "Hello!", "Hi, it's a pleasure talking to you."],
            },

            "goodbye": {
                "list": ["bye", "goodbye"],
                "answer": ["Goodbye!", "Bye, I hope have been useful.", "See you soon!"],
            },

            "name": {
                "list1": ["what", "how"],
                "list2": ["name", "call"],
                "answer": [
                    "My name is " + bot_name + ".", "You can call me " + bot_name + ".", "I'm " + bot_name + "."
                ],
            },

            "utility": {
                "list1": ["what"],
                "list2": ["do"],
                "answer":
                    "I can do many things, such as guide you around the venue or give you information about works and "
                    "authors, I am at your service."
            },

            "enclosure_hours": {
                "list1": ["museum", "enclosure", "open", "opening", "close", "closing"],
                "list2": ["time", "hours"],
                "answer":
                    "Museum hours are from " + opening_time + " to " + closing_time + "."
            },

            "location": {
                "list1": ["address", "location", "where"],
                "list2": ["museum", "enclosure", "building", "venue"],
                "list3": [""],
                "answer": "The address of the venue is: " + address
            },

            "date": {
                "list1": ["what"],
                "list2": ["date"],
                "answer": "Today is " + datetime.today().strftime('%d/%m/%Y')
            },

            "time": {
                "list1": ["what"],
                "list2": ["time"],
                "answer": "It's " + datetime.today().strftime('%H:%M')
            },

            "thanks": {
                "list": ["thank", "thanks"],
                "answer": "You're welcome, it's a pleasure to help you."
            },
        },


        "Spanish": {

            "not_understand": "Lo siento, no se a que se refiere. ¿Puede repetirlo por favor?",

            "move": {
                "move": [
                    "ir", "llevar", "llévame", "llevame", "llévanos", "llevanos", "conducir", "condúceme", "conduceme",
                    "condúcenos", "conducenos", "dirigir", "dirígeme", "dirigeme", "dirígete", "dirígete", "dirígenos",
                    "dirígenos", "mostrar", "muéstrame", "muestrame", "muéstranos", "muestranos",
                    "muévete", "muevete", "desplázate", "desplazate", "camina"
                ],
                "aux": ["camino", "ruta"],
                "answer": "Muy bien, por favor sígame.",
            },

            "info": [
                "información", "informacion", "info", "informar", "infórmame", "informame", "infórmanos", "informanos",
                "hablar", "háblame", "hablame", "háblanos", "hablanos", "contar", "cuéntame", "cuentame", "cuéntanos",
                "cuentanos", "decir", "decirme", "decirnos", "saber", "sabes", "conocer", "conoces"
            ],

            "show": {
                "show": [
                    "ver", "desplegar", "mostrar", "muéstrame", "muestrame", "muéstranos", "muestranos", "enseñar",
                    "enséñame", "enseñame", "enséñanos", "enseñanos"
                ],
                "map": ["mapa", "plano"],
                "answer": "Este es el mapa del recinto.",
            },

            "greetings": {
                "intro": "¡Hola! Mi nombre es " + bot_name + " ¿En que puedo ayudarle?",
                "list": ["hola", "hey", "saludos", "buenas"],
                "answer": ["¡Muy buenas!", "¡Hola!", "Hola es un placer hablar contigo"],
            },

            "goodbye": {
                "list": ["adiós", "adios", "chao"],
                "answer": ["¡Adios!", "Adios, espero haberte sido de utilidad.", "¡Hasta pronto!"],
            },

            "name": {
                "list1": ["cómo", "como", "cuál", "cual", "dime"],
                "list2": ["llamas", "llamarte", "nombre"],
                "answer": [
                    "Mi nombre es " + bot_name + ".", "Puedes llamarme " + bot_name + ".", "Soy " + bot_name + "."
                ],
            },

            "utility": {
                "list1": ["qué", "que"],
                "list2": ["sabes", "sirves", "usos", "puedes"],
                "answer":
                    "Puedo hacer muchas cosas, como guiarte por el recinto o darte información sobre obras y autores, "
                    "estoy a tu servicio."
            },

            "enclosure_hours": {
                "list1": ["hora", "horario"],
                "list2": ["museo", "recinto", "apertura", "abre", "cierra", "cierre"],
                "answer":
                    "El horario del museo es de " + opening_time + " a " + closing_time + "."
            },

            "location": {
                "list1": ["dirección", "direccion", "ubicación", "ubicacion", "donde"],
                "list2": ["está", "esta", "encuentra", "ubica"],
                "list3": ["museo", "recinto", "edificio"],
                "answer": "La dirección del recinto es: " + address
            },

            "date": {
                "list1": ["qué", "que"],
                "list2": ["fecha"],
                "answer": "Hoy es " + datetime.today().strftime('%d/%m/%Y')
            },

            "time": {
                "list1": ["qué", "que"],
                "list2": ["hora"],
                "answer": "Son las " + datetime.today().strftime('%H:%M')
            },

            "thanks": {
                "list": ["grácias", "gracias"],
                "answer": "De nada, es un placer poder ayudarte."
            },
        },


        "Portuguese": {

            "not_understand": "Desculpa nao sei o que queres dizer. Você pode repetir por favor?",

            "move": {
                "move": [
                    "vá", "va", "vai", "leve-me", "leve-nos", "direcione-me", "direcione-nos", "mostre-me",
                    "mostre-nos", "role", "caminhe",
                ],
                "aux": ["caminho", "estrada", "rua", "rota"],
                "answer": "Muito bom, por favor me siga.",
            },

            "info": [
                "informação", "informaçao", "info", "informe", "informe-me", "informe-nos", "fale", "diga", "diga-me",
                "diga-nos", "conheça"
            ],

            "show": {
                "show": [
                    "ver", "revelar", "mostrar", "mostrar-me", "mostrar-nos", "ensinar", "mostrar-me", "mostrar-nos"
                ],
                "map": ["mapa", "plano"],
                "answer": "Este é o mapa do recinto.",
            },

            "greetings": {
                "intro": "Olá! Meu nome é " + bot_name + ". Como posso ajudá-lo?",
                "list": ["olá", "ola", "ei", "saudações", "saudaçoes"],
                "answer": ["Bom dia!", "Olá!", "Olá, é um prazer falar com você"],
            },

            "goodbye": {
                "list": ["tchau"],
                "answer": ["Tchau!", "Tchau, espero ter sido útil para você.", "Até logo!"],
            },

            "name": {
                "list1": ["como", "qual", "diga-me"],
                "list2": ["chamá-lo", "chama-lo", "nome"],
                "answer": [
                    "Meu nome é " + bot_name + ".", "Você pode me chamar de " + bot_name + ".",
                    "Eu sou o " + bot_name + "."
                ],
            },

            "utility": {
                "list1": ["que"],
                "list2": ["sabe", "pode", "bom"],
                "answer":
                    "Posso fazer muitas coisas, como guiá-lo pelo local ou dar informações sobre obras e autores, "
                    "estou à sua disposição."
            },

            "enclosure_hours": {
                "list1": ["hora", "horário", "horário"],
                "list2": ["museu", "gabinete", "funcionamento", "fechamento", "fecho"],
                "answer":
                    "O horário do museu é de " + opening_time + " a " + closing_time + "."
            },

            "location": {
                "list1": ["endereço", "local", "onde", "localização", "localizaçao"],
                "list2": ["museu", "anexo", "edifício", "edificio", "local"],
                "list3": [""],
                "answer": "O endereço do local é: " + address
            },

            "date": {
                "list1": ["que"],
                "list2": ["data"],
                "answer": "Hoje é " + datetime.today().strftime('%d/%m/%Y')
            },

            "time": {
                "list1": ["que"],
                "list2": ["horas"],
                "answer": "São " + datetime.today().strftime('%H:%M')
            },
            "thanks": {
                "list": ["obrigado", "obrigada"],
                "answer": "De nada, é um prazer ajudá-lo."
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
