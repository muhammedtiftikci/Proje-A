

class SocketDataReader:
    def __init__(self, database):
        self._database = database

    def read(self, data):
        splitted_data = data.split(",")

        model = {
            'client_type': splitted_data[0],
            'username': splitted_data[1],
            'password': splitted_data[2],
            'latitude': splitted_data[3],
            'longitude': splitted_data[4]
        }

        return model

    def check_user(self, model):
        for x in self._database:
            if x['username'] == model['username'] and x['password'] == model['password']:
                return True

        return False