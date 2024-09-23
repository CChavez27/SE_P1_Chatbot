from fuzzywuzzy import process
import spacy
import json
import os

# Inicializamos el modelo de lenguaje de spaCy
nlp = spacy.load('en_core_web_sm')

DB_FILE = 'chatbot_db.json'

def load_database():
    if os.path.exists(DB_FILE):
        with open(DB_FILE, 'r') as file:
            return json.load(file)
    else:
        return {}

def save_database(database):
    with open(DB_FILE, 'w') as file:
        json.dump(database, file, indent=4)

# Preprocesamos las preguntas para obtener tokens lematizados y eliminar stopwords
def preprocess_text(text):
    doc = nlp(text)
    tokens = [token.lemma_.lower() for token in doc if not token.is_stop and not token.is_punct]
    return ' '.join(tokens)

# Obtener respuesta con fuzzy matching y spaCy
def get_response(database, question):
    preprocessed_question = preprocess_text(question)
    questions = list(database.keys())
    
    # Usamos fuzzywuzzy para buscar la coincidencia más cercana
    best_match, score = process.extractOne(preprocessed_question, questions)
    
    if score > 70:  # Umbral de coincidencia
        return database[best_match]
    else:
        return None

def add_knowledge(database, question, answer):
    preprocessed_question = preprocess_text(question)
    database[preprocessed_question] = answer
    save_database(database)

def chatbot():
    print("Chatbot iniciado. Escribe 'salir' para terminar el chat.")
    database = load_database()

    while True:
        question = input("Tú: ")

        if question.lower() == 'salir':
            print("¡Adiós!")
            break

        # Buscar respuesta en la base de datos
        response = get_response(database, question)

        if response:
            print(f"Chatbot: {response}")
        else:
            print("Chatbot: No tengo una respuesta para eso.")
            new_answer = input("¿Cuál sería una respuesta adecuada para esta pregunta?: ")
            add_knowledge(database, question, new_answer)
            print("Chatbot: ¡Gracias! He aprendido algo nuevo.")

if __name__ == '__main__':
    chatbot()
