"""Waypoint.py"""
class Waypoint():
    """
    A Waypoint is a known point within a given Route.

    Attributes:
        latitude: a double of range -90.0 (i.e. South) to +90.0 (i.e. North)
        longitude: a double of range -180.0 (i.e. West) to +180.0 (i.e. East)
        altitude: a double of boundless range of height against sea level
    """

    def __init__(self, in_latitude, in_longitude, in_altitude):
        self.set_latitude(in_latitude)
        self.set_longitude(in_longitude)
        self.set_altitude(in_altitude)

    @property
    def latitude(self):
        return self._latitude

    @latitude.setter
    def latitude(self, in_latitude):
        if in_latitude < -90.0 or in_latitude > 90.0:
            raise ValueError("Latitude is out of normal bounds")
        self.latitude = in_latitude

    @property
    def longitude(self):
        return self._longitude

    @longitude.setter
    def longitude(self, in_longitude):
        if in_longitude < -180.0 or in_longitude > 180.0:
            raise ValueError("Longitude is out of normal bounds")
        self.longitude = in_longitude

    @property
    def altitude(self):
        return self._altitude
