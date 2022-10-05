import socket

HOST = 'Host Public Address'
Port = 8080

sockets = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sockets.connect((HOST, Port))

sockets.send("Socket Done has been established".encode('Utf-8'))
print(sockets.recv(1024).decode('Utf-8'))
