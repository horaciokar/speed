# client_speed_test.py
import socket
import time

HOST = "10.86.110.1"
PORT = 5001
BUFFER = 65536

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

total_bytes = 0
start_time = time.time()
last_time = start_time

try:
    while True:
        data = client.recv(BUFFER)
        if not data:
            break

        total_bytes += len(data)

        now = time.time()

        if now - last_time >= 1:
            speed = total_bytes / (now - start_time)
            mbps = (speed * 8) / 1_000_000

            print(f"Velocidad: {mbps:.2f} Mbps")

            last_time = now

except KeyboardInterrupt:
    print("Test detenido")

client.close()
