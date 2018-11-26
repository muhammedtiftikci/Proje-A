from datetime import datetime


class Location:
    def __init__(self, latitude, longitude):
        self.__latitude = latitude
        self.__longitude = longitude

    @property
    def latitude(self):
        return self.__latitude

    @property
    def longitude(self):
        return self.__longitude

    @latitude.setter
    def latitude(self, value):
        self.__latitude = value

    @longitude.setter
    def longitude(self, value):
        self.__longitude = value

    def equals(self, location):
        latitudeEquals = self.__latitude = location.getLongitude()
        longitudeEquals = self.__longitude = location.getLongitude()

        return latitudeEquals and longitudeEquals


class DataModel:
    def __init__(self, username, location):
        self.__username = username
        self.__location = location
        self.__date = datetime.today()

    @property
    def username(self):
        return self.__username

    @property
    def location(self):
        return self.__location

    @location.setter
    def location(self, value):
        self.__date = datetime.today()
        self.__location = value


class LocationManager:
    def __init__(self):
        self._list = []

    def add_or_update(self, username, latitude, longitude):
        changed = False

        for item in self._list:
            if item.username == username:
                item.location = Location(latitude, longitude)

                changed = True

        if not changed:
            location = Location(latitude, longitude)
            item = DataModel(username, location)
            
            self._list.append(item)

    def getItemAt(self, index):
        return self._list[index]

    @property
    def length(self):
        return len(self._list)