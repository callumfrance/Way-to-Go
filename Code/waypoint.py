"""
Waypoint
"""

# Author: Callum France


class Waypoint:
    """A known point within a given Route.

    Attributes
    ----------
        _latitude : double
            range -90.0 (i.e. South) to +90.0 (i.e. North)

        _longitude : double
            range -180.0 (i.e. West) to +180.0 (i.e. East)

        _altitude : double
            boundless range of height against sea level
    """

    def __init__(self, in_latitude, in_longitude, in_altitude):
        self._latitude = in_latitude
        self._longitude = in_longitude
        self._altitude = in_altitude

    @property
    def latitude(self):
        """latitude property"""
        return self._latitude

    @latitude.setter
    def latitude(self, in_latitude):
        if isinstance(in_latitude, float):
            if -90.0 <= in_latitude <= 90.0:
                self._latitude = in_latitude
            else:
                raise ValueError("Latitude is out of normal bounds")
        else:
            raise TypeError("Latitude must be a float")

    @property
    def longitude(self):
        """longitude property"""
        return self._longitude

    @longitude.setter
    def longitude(self, in_longitude):
        if isinstance(in_longitude, float):
            if -180.0 <= in_longitude <= 180.0:
                self._longitude = in_longitude
            else:
                raise ValueError("Longitude is out of normal bounds")
        else:
            raise TypeError("Longitude must be a float")

    @property
    def altitude(self):
        """altitude property"""
        return self._altitude

    @altitude.setter
    def altitude(self, in_altitude):
        if not isinstance(in_altitude, float):
            raise TypeError("Altitude must be a float")
        else:
            self._altitude = in_altitude

     def __str__(self):
       return '{} {} {}'.format(self._latitude, self._longitude, self._altitude)
