import socket

HOST = "127.0.0.1"
PORT = 37037
BUFFER_SIZE = 1024

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))

client_socket.sendall("Hello from client.")

received_data = client_socket.recv(BUFFER_SIZE)

print(received_data)

client_socket.close()