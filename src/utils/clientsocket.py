import socket

class ClientSocket:
    def __init__(self, host, port, buffer_size):
        self.__host = host
        self.__port = port
        self.__buffer_size = buffer_size

    def get_locations(self, latitude, longitude):
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((self.__host, self.__port))

        data_list = [
            "raspberry",
            "",
            "",
            latitude,
            longitude
        ]

        data = ",".join(data_list)

        client_socket.sendall(data)

        received_data = client_socket.recv(self.__buffer_size)

        client_socket.close()

        if received_data == "NO":
            return []

        return [ m.split(',') for m in received_data.split(";") ]
