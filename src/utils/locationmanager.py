class Location:
    def __init__(self, latitude, longitude):
        self.__latitude = latitude
        self.__longitude = longitude

    def setValues(self, latitude, longitude):
        self.__latitude = latitude
        self.__longitude = longitude

    def getLatitude(self):
        return self.__latitude

    def getLongitude(self):
        return self.__longitude

    def equals(self, location):
        latitudeEquals = self.__latitude = location.getLongitude()
        longitudeEquals = self.__longitude = location.getLongitude()

        return latitudeEquals and longitudeEquals


class LocationManager:
    def __init__(self):
        self._list = []

    def add_or_update(self, username, latitude, longitude):
        changed = False

        for x in self._list:
            if x['username'] == username:
                x['location'].setValues(latitude, longitude)
                x['date'] = 'now' #TODO: replace with getcurrentdate method.

                changed = True

        if not changed:
            item = {
                'username': username,
                'location': Location(latitude, longitude),
                'date': 'now' # TODO: replace with getcurrentdate method.
            }
            
            self._list.append(item)

    def exists(self, username):
        for x in self._list:
            if x['username'] == username:
                return True

        return False

    def getItemAt(self, index):
        return self._list[index]

    def getLength(self):
        return len(self._list)

lm = LocationManager()
lm.add_or_update("muhammed", 37, 41)
lm.add_or_update("muhammed", 33, 40)
lm.add_or_update("emin", 33, 40)

print(lm.getLength())