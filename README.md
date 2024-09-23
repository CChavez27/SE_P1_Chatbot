# Chatbot de Aprendizaje

Este es un chatbot simple que utiliza `fuzzywuzzy` y `spaCy` para aprender nuevas respuestas y mantener un diálogo con el usuario.

## Requisitos

Antes de ejecutar el proyecto, asegúrate de tener instalado Python en tu sistema. Este proyecto ha sido probado con Python 3.x.

## Instalación

Sigue estos pasos para instalar las bibliotecas necesarias:

1. **Clona el repositorio:**
   ```bash
   https://github.com/CChavez27/SE_P1_Chatbot.git

2. **Instala las librerías requeridas:**
   ```bash
   pip install fuzzywuzzy[speedup]
   pip install spacy
   
2. **Descarga el modelo de lenguaje de spaCy:**
   ```bash
   python -m spacy download en_core_web_sm

Uso
Una vez que hayas instalado las bibliotecas, puedes ejecutar el código principal con el siguiente comando:

bash
Copiar código
python Main.py
El chatbot comenzará y podrás interactuar con él. Escribe "salir" en cualquier momento para terminar la conversación.
