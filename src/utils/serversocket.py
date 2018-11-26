import socket
from assets import Location
from assets import DataModel
from assets import LocationManager
from socketdatareader import SocketDataReader


database = [
    { 'username': 'muhammed', 'password': '123456' },
    { 'username': 'tiftikci', 'password': '123456' }
]

data_reader = SocketDataReader(database)
location_manager = LocationManager()


HOST = "0.0.0.0"
PORT = 37037
BUFFER_SIZE = 1024

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen(10)

while True:
    connected_socket, addr = server_socket.accept()

    print("A client connected:", addr)

    received_data = connected_socket.recv(BUFFER_SIZE)

    model = data_reader.read(received_data)

    if model['client_type'] == "android":
        if data_reader.check_user(model):
            print("Username: " + model['username'])
            print("Latitude: " + model['latitude'])
            print("Longitude: " + model['longitude'])

            location_manager.add_or_update(model['username'], model['latitude'], model['longitude'])

            connected_socket.sendall("OK")
        else:
            connected_socket.sendall("ERR")



    elif client_type == "raspberry":
        pass

server_socket.close()