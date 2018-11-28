import socket
import time

HOST = "127.0.0.1"
PORT = 37037
BUFFER_SIZE = 1024
DELAY_TIME = 5

CLIENT_TYPE = "raspberry"
LATITUDE = "35"
LONGITUDE = "-120"


def get_locations(latitude, longitude):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((HOST, PORT))

    data_list = [
        CLIENT_TYPE,
        "",
        "",
        latitude,
        longitude
    ]

    data = ",".join(data_list)

    client_socket.sendall(data)

    received_data = client_socket.recv(BUFFER_SIZE)

    client_socket.close()

    if received_data == "NO":
        return []

    return [ m.split(',') for m in received_data.split(";") ]


while True:
    locations = get_locations(LATITUDE, LONGITUDE)

    print(locations)

    time.sleep(DELAY_TIME)