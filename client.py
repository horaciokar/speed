import socket
import time

SERVER = "backnetlabs.net.ar"
PORT = 5001

client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

client.connect((SERVER,PORT))

while True:

    msg = input("Mensaje: ")

    if msg == "exit":
        break

    client.send(msg.encode())

client.close()