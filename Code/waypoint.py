"""
Waypoint
"""

# Author: Callum France

class Waypoint():
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
        self.latitude = in_latitude
        self.longitude = in_longitude
        self.altitude = in_altitude


    @property
    def latitude(self):
        """latitude property"""
        return self.latitude

    @latitude.setter
    def latitude(self, in_latitude):
        if isinstance(in_latitude, float):
            if in_latitude > -90.0 and in_latitude < 90.0:
                self.latitude = in_latitude
            else:
                raise ValueError("Latitude is out of normal bounds")
        else:
            raise ValueError("Latitude is out of normal bounds")

    @property
    def longitude(self):
        """longitude property"""
        return self.longitude

    @longitude.setter
    def longitude(self, in_longitude):
        if isinstance(in_longitude, float):
            if in_longitude > -180.0 and in_longitude < 180.0:
                self.longitude = in_longitude
            else:
                raise ValueError("Longitude is out of normal bounds")
        else:
            raise ValueError("Longitude is out of normal bounds")

    @property
    def altitude(self):
        """altitude property"""
        return self.altitude
