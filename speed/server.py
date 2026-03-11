# server_speed_test.py

import socket

HOST = "0.0.0.0"
PORT = 5002
BUFFER = 65536

data = b'0' * BUFFER

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen(5)

print(f"\nServidor escuchando en {HOST}:{PORT}\n")

while True:

    conn, addr = server.accept()

    ip_cliente = addr[0]
    puerto_cliente = addr[1]

    print("===================================")
    print("Cliente conectado")
    print(f"IP origen: {ip_cliente}")
    print(f"Puerto origen: {puerto_cliente}")
    print(f"Puerto destino: {PORT}")
    print("Protocolo: TCP")
    print("Capa OSI: Transporte (L4)")
    print("===================================\n")

    try:
        while True:
            conn.sendall(data)

    except BrokenPipeError:
        print(f"Cliente {ip_cliente} desconectado\n")

    conn.close()