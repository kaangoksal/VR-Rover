import time
import socket
import sys
import json


HOST, PORT = "umb.kaangoksal.com", 5005



sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

sock.connect((HOST, PORT))
print("Sending to", HOST, " ", PORT)
# Prints the values for axis0
sock.sendall("kaan")
while True:
    data, addr = sock.recvfrom(1024)  # buffer size is 1024 bytes
    print("received message:", data, addr)

