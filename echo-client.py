# echo-client.py

import socket

HOST = "192.168.0.103"  # The server's hostname or IP address
PORT = 9876  # The port used by the server

while 1:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        s.sendall(b"TRIGGER")
        data = s.recv(1024)

    print("Received " + data.decode())
