from datetime import datetime
import math
import settings


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


class DataModel(object):
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
        self.__date = datetime.now()
        self.__location = value


    def is_near(self, location, max_distance, now, deltatime):
        dx = self.__location.latitude - location.latitude
        dy = self.__location.longitude - location.longitude

        if now - self.__date > deltatime:
            print("Time...")
            return False

        print(math.sqrt((dx * dx) + (dy * dy)), max_distance)

        return math.sqrt((dx * dx) + (dy * dy)) < max_distance


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

    def search(self, latitude, longitude):
        location = Location(latitude, longitude)

        now = datetime.now()

        near_data_models = []

        for data_model in self._list:
            if data_model.is_near(location, settings.MAX_DISTANCE, now, settings.DELTA_TIME):
                near_data_models.append(data_model)

        return near_data_models