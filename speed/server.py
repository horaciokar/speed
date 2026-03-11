# server_speed_test.py
import socket

HOST = "0.0.0.0"
PORT = 5002
BUFFER = 65536  # 64 KB

data = b'0' * BUFFER

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen(1)

print(f"Servidor escuchando en {HOST}:{PORT}")

conn, addr = server.accept()
print(f"Cliente conectado: {addr}")

try:
    while True:
        conn.sendall(data)
except BrokenPipeError:
    print("Cliente desconectado")

conn.close()
server.close()
