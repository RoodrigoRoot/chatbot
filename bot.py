"""
Chatbot to register a Movie
"""

from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

movies = ChatBot("Rod",

    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    database_uri='sqlite:///database.sqlite3'
)
trainer = ListTrainer(movies)

RESPONSE = "Hola, ¿Deseas apartar una entrada para una pelicula?"


SHOW_CATALOG = """
1.- Black Widow\n
2.- Escuadrón Suicida 2\n
3.- Un Jefe en Pañales\n
"""

talk1 = ["Que onda", RESPONSE]
talk2 = ["Hola", RESPONSE]
talk3 = ["Buenas tardes", RESPONSE]
talk4 = ["Que tal", RESPONSE]
talk5 = ["Holis",RESPONSE]
talk6 = ["Hola, Buenas", RESPONSE]
talk7 = ["Buenas días",RESPONSE]
talk8 = ["buenos dias", RESPONSE]
talk9 = ["buenas buenas", RESPONSE]
talk10 = ["buenas noches", RESPONSE]
talk11 = ["buenas", RESPONSE]
talk11 = ["saludos", RESPONSE]

movies1 = ["si", SHOW_CATALOG]
movies2 = ["si, quiero apartar una", SHOW_CATALOG]
movies3 = ["si, por favor", SHOW_CATALOG]
movies4 = ["si, gracias", SHOW_CATALOG]
movies5 = ["claro", SHOW_CATALOG]
movies6 = ["afirmativo", SHOW_CATALOG]

tanks1 = ["Gracias", "Fue un place atenderte"]
tanks2 = ["Perfecto", "Fue un place atenderte"]
tanks3 = ["Genial", "Fue un place atenderte"]
tanks4 = ["vale", "Fue un place atenderte"]


trainer.train(talk1)
trainer.train(talk2)
trainer.train(talk3)
trainer.train(talk4)
trainer.train(talk5)
trainer.train(talk6)
trainer.train(talk7)
trainer.train(talk8)
trainer.train(talk9)
trainer.train(talk10)
trainer.train(talk11)


trainer.train(movies1)
trainer.train(movies2)
trainer.train(movies3)
trainer.train(movies4)
trainer.train(movies5)
trainer.train(movies6)

trainer.train(tanks1)
trainer.train(tanks2)
trainer.train(tanks3)
trainer.train(tanks4)

def movie_reservation(connection, data):
    connection.sendall("¿Cual es tu nombre?".encode())
    data = connection.recv(1024)
    data = data.decode("utf-8")
    return f"Se ha registrado su reservación, {data}"



"""while True:
    msg = input("Tu: ")

    try:
        option = int(msg)
        response = movie_reservation(option)
        print(response)
        continue
    except Exception as e:
        print("se va pa' ca")
    response = movies.get_response(msg)
    print("Bot:", response)
"""


