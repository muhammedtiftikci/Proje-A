import socket

HOST = "127.0.0.1"
PORT = 37037
BUFFER_SIZE = 1024

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen(10)

connected_socket, addr = server_socket.accept()

print("A client connected:", addr)

received_data = connected_socket.recv(BUFFER_SIZE)

print(received_data)

connected_socket.sendall("Hello from server.")

server_socket.close()