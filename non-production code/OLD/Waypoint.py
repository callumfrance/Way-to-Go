"""Waypoint.py"""
class Waypoint():
    """
    A Waypoint is a known point within a given Route.

    Attributes:
        latitude: a double of range -90 (i.e. South) to +90 (i.e. North)
        longitude: a double of range -180 (i.e. West) to +180 (i.e. East)
        altitude: a double of boundless range of height against sea level
    """

    def __init__(self, in_latitude, in_longitude, in_altitude):
        self.set_latitude(in_latitude)
        self.set_longitude(in_longitude)
        self.set_altitude(in_altitude)

    # ---------
    # Accessors
    # ---------
    def get_latitude(self):
        """Returns latitude."""
        return self.latitude

    def get_longitude(self):
        """Returns longitude."""
        return self.longitude

    def get_altitude(self):
        """Returns altitude."""
        return self.altitude

    # --------
    # Mutators
    # --------
    def set_latitude(self, in_latitude):
        """Validates and sets latitude."""
        if in_latitude < -90 or in_latitude > 90:
            raise ValueError("Latitude is out of normal bounds")
        self.latitude = in_latitude

    def set_longitude(self, in_longitude):
        """Validates and sets longitude."""
        if in_longitude < -180 or in_longitude > 180:
            raise ValueError("Longitude is out of normal bounds")
        self.longitude = in_longitude

    def set_altitude(self, in_altitude):
        """Validates and sets altitude."""
        self.altitude = in_altitude
