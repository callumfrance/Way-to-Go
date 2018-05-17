import sys
sys.path.append('../..')
from GeoUtils import GeoUtils
"""
Waypoint
"""
__author__ = 'Callum France'


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
        self.latitude = in_latitude
        self.longitude = in_longitude
        self.altitude = in_altitude
        # print("\nWaypoint is: {},{},{}".format(self.latitude, self.longitude,
        #                                        self.altitude))

    @property
    def latitude(self):
        """latitude property"""
        return self._latitude

    @latitude.setter
    def latitude(self, in_latitude):
        if not isinstance(in_latitude, float):
            raise TypeError("Latitude must be a float")
        if not -90.0 <= in_latitude <= 90.0:
            raise ValueError("Latitude must be between -90.0 and 90.0")
        self._latitude = in_latitude

    @property
    def longitude(self):
        """longitude property"""
        return self._longitude

    @longitude.setter
    def longitude(self, in_longitude):
        if not isinstance(in_longitude, float):
            raise TypeError("Longitude must be a float")
        if not -180.0 <= in_longitude <= 180.0:
            raise ValueError("Longitude must be between -180.0 and 180.0")
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

    def calc_metres_diff(self, next_segment):
        x = self.calc_metres_dist(next_segment)
        x.extend(self.calc_metres_vertical(next_segment))
        return x

    def calc_metres_dist(self, next_segment=None):
        """Calls GeoUtils for two points along a route.

        Arguments:
            next_segment : Segment
                The other 'waypoint' value to find distance between.

        Returns:
            dist : float
                Represents the distance on Earth between two horizontal points.
        """
        dist = 0.0
        if next_segment is not None:
            dist = GeoUtils.calcMetresDistance(self.latitude, self.longitude,
                                               next_segment.latitude,
                                               next_segment.longitude)
        return dist

    def calc_metres_ascent(self, next_segment):
        return (self.calc_metres_vertical())[0]

    def calc_metres_descent(self, next_segment):
        return (self.calc_metres_vertical())[1]

    def calc_metres_vertical(self, next_segment=None):
        """Determines if the segment is a climb or descent, returning the value.

        Arguments:
            next_segment : Segment
                The other 'waypoint' value to find vertical distance between.

        Returns:
            seg_vert : float[2]
                seg_vert[0] is the climb distance
                seg_vert[1] is the descent distance
                One value will always be 0 - only one can change per segment.
        """
        seg_vert = [0.0, 0.0]
        if next_segment is not None:
            x = next_segment.altitude - self.altitude
            if x > 0.0:
                seg_vert[0] = x
            else:
                seg_vert[1] = -x
        return seg_vert

    def __str__(self):
        return '{},{},{}'.format(self.latitude, self.longitude,
                                 self.altitude)

    def __eq__(self, in_wp):
        """Checks if an incoming waypoint is'close enough'
        so that both Waypoints can be considered 'the same'.

        They are the same if within 10 m horizontal AND 2 m vertically.
        """
        is_equal = False
        # if self.calc_metres_dist(in_wp) <= 10.0 and \
        #         self.calc_metres_vertical(in_wp) <= 2.0:
        if self.calc_metres_dist(in_wp) <= 10.0:
            if self.calc_metres_vertical(in_wp)[0] <= 2.0 and \
                    self.calc_metres_vertical(in_wp)[1] <= 2.0:
                is_equal = True
        return is_equal
