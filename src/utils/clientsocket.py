import socket

HOST = "127.0.0.1"
PORT = 37037
BUFFER_SIZE = 1024

CLIENT_TYPE = "android"
USERNAME = "muhammed"
PASSWORD = "123456"
LOCATION_E = "37"
LOCATION_B = "41"

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))

data_list = [
    CLIENT_TYPE,
    USERNAME,
    PASSWORD,
    LOCATION_E,
    LOCATION_B
]

data = ",".join(data_list)

client_socket.sendall(data)

received_data = client_socket.recv(BUFFER_SIZE)

if received_data == "OK":
    print("Data sent.")
elif received_data == "ERR":
    print("An error occured!")

client_socket.close()