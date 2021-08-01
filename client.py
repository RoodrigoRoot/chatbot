import socket

clientsocket = socket.socket()

host = "127.0.0.1"
port = 1233


print("waiting for concection")
try:
    clientsocket.connect((host, port))
except Exception as e:
    print(e)


Response = clientsocket.recv(1024)

while True:
    Input = input("Tu: ")
    clientsocket.send(str.encode(Input))
    response = clientsocket.recv(1024)
    print("Bot", response.decode("utf-8"))

clientsocket.close()