"""
Waypoint
"""

# Author: Callum France


class Waypoint:
    """A known point within a given Route.

    Attributes
    ----------
        latitude : double
            range -90.0 (i.e. South) to +90.0 (i.e. North)

        longitude : double
            range -180.0 (i.e. West) to +180.0 (i.e. East)

        altitude : double
            boundless range of height against sea level
    """

    def __init__(self, in_latitude, in_longitude, in_altitude):
        print("{} {} {}".format(in_latitude, in_longitude, in_altitude))
        self.latitude = in_latitude
        self.longitude = in_longitude
        self.altitude = in_altitude

    @property
    def latitude(self):
        """latitude property"""
        return self._latitude

    @latitude.setter
    def latitude(self, in_latitude):
        if not isinstance(in_latitude, float):
            raise TypeError
        if not -90.0 <= in_latitude <= 90.0:
            raise ValueError
        self._latitude = in_latitude

    @property
    def longitude(self):
        """longitude property"""
        return self._longitude

    @longitude.setter
    def longitude(self, in_longitude):
        if not isinstance(in_longitude, float):
            raise TypeError
        if not -180.0 <= in_longitude <= 180.0:
            raise ValueError
        self._longitude = in_longitude

    @property
    def altitude(self):
        """altitude property"""
        return self._altitude

    @altitude.setter
    def altitude(self, in_altitude):
        if not isinstance(in_altitude, float):
            raise TypeError("Altitude must be a float")
        self._altitude = in_altitude

    @altitude.setter
    def altitude(self, in_altitude):
        if not isinstance(in_altitude, float):
            raise TypeError
        self._altitude = in_altitude

    def __str__(self):
        return '{},{},{}'.format(self._latitude, self._longitude,
                                 self._altitude)
