import socket
from _thread import *
from bot import movies, movie_reservation

serversocket = socket.socket()

host = "127.0.0.1"
port = 1233

ThreadCount = 0

is_connect = True

try:
    serversocket.bind((host, port))
    serversocket.listen(5)
except Exception as e:
    is_connect = False

if is_connect:
    print("Running.......")
else:
    print("Problems with the host")

def client_thread(connection):
    connection.send(str.encode("Reservación de Entradas de Cine"))
    while True:
        data = connection.recv(1024)
        data = data.decode("utf-8")
        connection.settimeout(15)
        reply = ""
        try:
            data = int(data)
            reply = movie_reservation(connection, data)
            connection.sendall(str.encode(reply))
            continue
        except Exception as e:
            reply = movies.get_response(data)

        if not data:
            break

        connection.sendall(str.encode(reply.text))
    connection.close()

while is_connect:
    client, address = serversocket.accept()
#    print("Connecteed to:" + address[0] + " " + str(address[1]))
    start_new_thread(client_thread, (client, ))
 #   ThreadCount += 1
 #   print("ThreadCount: ", str(ThreadCount))

serversocket.close()

