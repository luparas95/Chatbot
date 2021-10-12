from classes.DatabaseManager import DatabaseManager


db = DatabaseManager()
rows = db.execute('SELECT COUNT(*) FROM Artwork', "", 2)

print(rows)

db.close_conn()


"""import spacy

# Texto de entrada
texts = ["qual é a localização do museu"]
idiom = "pt"

# carga el paquete con las palabras del diccionario
if idiom == "en":
    nlp = spacy.load("en_core_web_lg")
elif idiom == "es":
    nlp = spacy.load("es_core_news_lg")
else:
    nlp = spacy.load("pt_core_news_lg")

for text in texts:
    # Procesa el texto de entrada
    doc = nlp(text)
    print(doc)

    # Muestra los atributos que ha detectado spaCy de cada palabra
    for token in doc:
        token_text = token.text
        token_pos = token.pos_
        token_dep = token.dep_

        print("{:<12}{:<10}{:<10}".format(token_text, token_pos, token_dep))"""


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
