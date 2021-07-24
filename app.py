from chatterbot import ChatBot, conversation
from chatterbot.trainers import ChatterBotCorpusTrainer, ListTrainer
import hug

####
#!/usr/bin/env python3

####class CORSRequestHandler (SimpleHTTPRequestHandler):
####    def end_headers (self):
####        self.send_header('Access-Control-Allow-Origin', '*')
####        SimpleHTTPRequestHandler.end_headers(self)

####if __name__ == '__main__':
####    test(CORSRequestHandler, HTTPServer, port=int(sys.argv[1]) if len(sys.argv) > 1 else 8000)
####

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

@hug.response_middleware()
def process_data(request, response, resource):
      response.set_header('Access-Control-Allow-Origin', '*')

@hug.get('/users', versions=1)
def user(user_id):
    return 'I do nothing useful.'
    #return user_id

@hug.get(examples='respuestapi?pregunta=holanda&id=1')
@hug.local()
def respuestapi(pregunta: hug.types.text, id: hug.types.number, hug_timer=3):
    respuesta = chatbot.get_response(pregunta)
    rrr=str(respuesta)
    return  {
                'id': id,
                'pregunta': pregunta,
                'respuesta': rrr,
                'took': float(hug_timer)
            }

if __name__ == '__main__':
    user.interface.local()
