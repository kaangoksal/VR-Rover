import time
import os
import socket
import fcntl
import struct
import json


def get_ip_address(ifname):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    return socket.inet_ntoa(fcntl.ioctl(
        s.fileno(),
        0x8915,  # SIOCGIFADDR
        struct.pack('256s', ifname[:15])
    )[20:24])

def get_lan_ip():
    ip = socket.gethostbyname(socket.gethostname())
    if ip.startswith("127.") and os.name != "nt":
        interfaces = ["eth0", "eth1", "eth2", "wlan0", "wlan1", "wifi0", "ath0", "ath1", "ppp0"]
        for ifname in interfaces:
            try:
                ip = get_ip_address(ifname)
                break
            except IOError:
                pass
    return ip


UDP_IP = get_lan_ip()
UDP_PORT = 5005

sock = socket.socket(socket.AF_INET,  # Internet
                     socket.SOCK_DGRAM)  # UDP
sock.bind((UDP_IP, UDP_PORT))
print("Started on ", UDP_IP, " ", UDP_PORT)
while True:
    data, addr = sock.recvfrom(1024)  # buffer size is 1024 bytes
    if data is not None:
        print("received message:", data, addr)
        sock.sendto(data + "sent back", addr)
        while True:
            sock.sendto("Ping", addr)
            time.sleep(10)



