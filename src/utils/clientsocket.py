import socket
import time

HOST = "127.0.0.1"
PORT = 37037
BUFFER_SIZE = 1024
DELAY_TIME = 5

CLIENT_TYPE = "raspberry"
LATITUDE = "23"
LONGITUDE = "45"

def send_location():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((HOST, PORT))

    data_list = [
        CLIENT_TYPE,
        LATITUDE,
        LONGITUDE
    ]

    data = ",".join(data_list)

    client_socket.sendall(data)

    received_data = client_socket.recv(BUFFER_SIZE)

    if received_data == "OK":
        print("Data sent.")
    elif received_data == "ERR":
        print("An error occured!")

    client_socket.close()

while True:
    send_location()
    time.sleep(DELAY_TIME)