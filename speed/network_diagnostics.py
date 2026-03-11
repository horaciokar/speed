# network_diagnostics.py

import socket
import subprocess
import os

SERVER = "IP_DEL_SERVIDOR"

print("\n=========== CAPA RED (L3) ===========\n")

hostname = socket.gethostname()
ip_local = socket.gethostbyname(hostname)

print(f"Host: {hostname}")
print(f"IP local: {ip_local}")

print("\n=========== GATEWAY ===========\n")

subprocess.run("ip route", shell=True)

print("\n=========== TABLA ARP (CAPA 2) ===========\n")

subprocess.run("arp -a", shell=True)

print("\n=========== TRACEROUTE ===========\n")

subprocess.run(f"traceroute {SERVER}", shell=True)

print("\n=========== PING RTT ===========\n")

subprocess.run(f"ping -c 4 {SERVER}", shell=True)