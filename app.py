from chatterbot import ChatBot, conversation
from chatterbot.trainers import ChatterBotCorpusTrainer, ListTrainer
from flask import Flask, request
app = Flask(__name__)
PORT = 8000
DEBUG = True

#se graba en log todo
import logging
logging.basicConfig(filename='archivolog.log', level=logging.DEBUG)
#se graba en log todo

#objeto de chatterbot
chatbot = ChatBot('WinChat')

#para borrar cache de aprendizaje
chatbot.storage.drop() #para borrar cache de aprendizaje

#####añadido de listas
entrenador = ListTrainer(chatbot)
conversacionL = ["Holanda", "Hola Humano"] #para entrenar con un array
entrenador.train(conversacionL)
#####añadido de listas

#url YML C:\Users\helto\AppData\Local\Programs\Python\Python39\Lib\site-packages\chatterbot_corpus\data

#entrena con archivos YML
entrenador = ChatterBotCorpusTrainer(chatbot)
entrenador.train("./data/roca.yml")
#entrenador.train(
#    "./data/propio.json"
#)
#entrena con archivos YML

#http://localhost:8000/respuestapi?pregunta=holanda&id=1
#hug -f .\app.py

@app.errorhandler(404)
def not_found(error):
    return "Not Found."

@app.route('/', methods=['GET'])
def index():
    return "Bienvenido a la API del futuro: EJ: (URL/id/pregunta)"   

@app.route('/<int:idd>/<string:p>', methods=['GET'])
def entity(idd, p):
    respuesta = chatbot.get_response(p)
    rrr=str(respuesta)
    return {
                'id': idd,
                'pregunta': p,
                'respuesta': rrr
            }

if __name__ == '__main__':
    app.run(port = PORT, debug = DEBUG)
