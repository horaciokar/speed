# client_speed_test.py

import socket
import time

SERVER = "backnetlabs.net.ar"
PORT = 5002
BUFFER = 65536

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

print("\nConectando al servidor...\n")

sock.connect((SERVER, PORT))

print("Conectado\n")

start = time.time()
total_bytes = 0

try:

    while True:

        t1 = time.time()

        data = sock.recv(BUFFER)

        t2 = time.time()

        if not data:
            break

        total_bytes += len(data)

        elapsed = time.time() - start

        velocidad = (total_bytes * 8) / (elapsed * 1000000)

        rtt = (t2 - t1) * 1000

        print(f"Velocidad: {velocidad:.2f} Mbps | RTT: {rtt:.2f} ms", end="\r")

except KeyboardInterrupt:

    print("\nCliente detenido")

sock.close()