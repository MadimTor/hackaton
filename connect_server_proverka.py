import socket


def connect(ip):
    sock = socket.socket()
    sock.connect((ip,9095))
    data = sock.recv(1024).decode()
    print(data)





