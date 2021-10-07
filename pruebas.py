"""import sqlite3
from os import path, getcwd
from spacy import load

DATABASE_PATH = path.join(getcwd(), "data/chatbotBBDD.sqlite")

nlp = load("es_core_news_lg")
db = sqlite3.connect(DATABASE_PATH)
cursor = db.cursor()

cursor.execute('SELECT * FROM Language WHERE Name = ?', ("spanish",))
rows = cursor.fetchall()


print(rows)"""


import spacy

# Texto de entrada
text = "print User super_admin"

# carga el paquete con las palabras del diccionario
nlp = spacy.load("en_core_web_lg")

# Procesa el texto de entrada
doc = nlp(text)

# Muestra los atributos que ha detectado spaCy de cada palabra
for token in doc:
    token_text = token.text
    token_pos = token.pos_
    token_dep = token.dep_

    print("{:<12}{:<10}{:<10}".format(token_text, token_pos, token_dep))


"""
from werkzeug.security import generate_password_hash, check_password_hash

texto = "1234"
texto_encriptado = generate_password_hash(texto)

print(texto_encriptado)
print(len(texto_encriptado))
"""

"""
patron = [
    {"LOWER": {"IN": ["ir", "condúceme", "llévame"]}},
    {"POS": "ADP", "OP": "?"},
    {"POS": "DET", "OP": "?"},
    {"LOWER": {"IN": ["entrada", "salida", "servicio"]}}
]
"""
