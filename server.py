import socket
import uuid
import subprocess
import base64
import hashlib

HOST = "0.0.0.0"
PORT = 5001


def get_server_mac():
    mac = uuid.getnode()
    mac = ':'.join(('%012X' % mac)[i:i+2] for i in range(0,12,2))
    return mac


def get_client_mac(ip):

    try:
        result = subprocess.check_output(["arp","-n",ip]).decode()

        for line in result.split("\n"):
            if ip in line:
                parts = line.split()
                return parts[2]

    except:
        pass

    return "No disponible (cliente fuera de LAN)"


def presentation_layer(data):

    print("\nCAPA 6 - PRESENTACION")

    text = data.decode("utf-8","ignore")

    print("Texto:", text)

    print("HEX:", data.hex())

    print("BASE64:", base64.b64encode(data).decode())

    print("SHA256:", hashlib.sha256(data).hexdigest())


def start_server():

    server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

    server.bind((HOST,PORT))

    server.listen(5)

    print("Servidor escuchando en puerto",PORT)

    while True:

        conn, addr = server.accept()

        client_ip = addr[0]
        client_port = addr[1]

        print("\n=================================")
        print("NUEVA SESION TCP")
        print("=================================")

        print("\nCAPA 7 - APLICACION")
        print("Aplicacion laboratorio redes")

        print("\nCAPA 5 - SESION")
        print("Sesion TCP activa")

        print("\nCAPA 4 - TRANSPORTE")
        print("TCP")
        print("Puerto origen:",client_port)
        print("Puerto destino:",PORT)

        print("\nCAPA 3 - RED")
        print("IP origen:",client_ip)

        print("\nCAPA 2 - ENLACE")
        print("MAC servidor:",get_server_mac())
        print("MAC cliente:",get_client_mac(client_ip))

        print("\nEsperando datos...\n")

        while True:

            data = conn.recv(4096)

            if not data:
                print("\nCliente cerro la sesion TCP")
                break

            presentation_layer(data)

        conn.close()


start_server()