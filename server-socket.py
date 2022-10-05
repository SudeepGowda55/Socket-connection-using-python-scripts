# !/bin/python3
from socketserver import UDPServer
import sys, socket

# for line in sys.stdin:
#     if line.rstrip() == "sudeep":
#         print("My Name is Sudeep Gowda")
#     if line.rstrip() == 'exit':
#         sys.exit()
#     if line.rstrip() == 'q':
#         sys.exit()
#     print(f"Input : {line}")
# sys.stdout.write('sudeep')


localipaddress = '0.0.0.0'
port = 8080 

# In AWS please add additional Inbound Rule for TCP 

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# socket.SOCK_DGRAM --> UDP
# socket.SOCK_STREAM --> TCP
server_socket.bind((localipaddress, port))
server_socket.listen(5)
while True :
    client_socket , client_address = server_socket.accept()
    print(f"Connected to {client_address}")
    message = client_socket.recv(1024).decode('Utf-8')
    print(f"Message from client is: {message}")
    client_socket.send("Got your message".encode('Utf-8'))
    client_socket.close()
    print(f"Connection with {client_address} ended")
    sys.exit()
