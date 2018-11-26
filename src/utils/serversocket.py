import socket
from locationmanager import LocationManager

database = ({ 'username': 'muhammed', 'password': '123456' })

class SocketDataReader:
    def __init__(self, database):
        self._database = database

    def read(self, data):
        splitted_data = data.split(",")

        model = {
            'client_type': splitted_data[0],
            'username': splitted_data[1],
            'password': splitted_data[2],
            'location_e': splitted_data[3],
            'location_b': splitted_data[4]
        }

        return model

    def check_user(self, model):
        for x in self._database:
            if x['username'] == model['username'] & x['password'] == model['password']:
                return True

        return False


data_reader = SocketDataReader(database)
location_manager = LocationManager()

locations = []


HOST = "0.0.0.0"
PORT = 37037
BUFFER_SIZE = 1024

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen(10)

connected_socket, addr = server_socket.accept()

print("A client connected:", addr)

received_data = connected_socket.recv(BUFFER_SIZE)

model = data_reader.read(received_data)

print(model)

if model['client_type'] == "android":
    if data_reader.check_user(model):
        location_manager.add_or_update(model['username'], model['latitude'], model['longitude'])

        connected_socket.sendall("OK")
    else:
        connected_socket.sendall("ERR")



elif client_type == "raspberry":
    pass

connected_socket.sendall("Hello from server.")

server_socket.close()