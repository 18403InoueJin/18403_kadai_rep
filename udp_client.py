import socket

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as hensuu:
    hensuu.sendto(b'Hello UDP world', ('127.0.0.1', 50007))