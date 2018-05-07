"""
Description
"""

# Author: Callum France

from segment import Segment
from waypoint import Waypoint
from GeoUtils import GeoUtils


class Description(Waypoint, Segment):
    """
    A description is the leaf node in the Segment composite pattern.

    It is a segment that can not be represented by a route, but simply
    by a description.

    Attributes
    ----------
        description : String
            A worded summary of the segment from the point in the route.
            Cannot start with an asterisk, and it can also not contain
            any newlines.
            Can be empty (for an end waypoint in a route).
    """
    def __init__(self, in_lat, in_long, in_alt, in_desc=""):
        try:
            Waypoint.__init__(self, in_lat, in_long, in_alt)
            self.description = in_desc
            # print("\nDescription is: {}".format(self.description))
        except TypeError as e:
            raise TypeError("Description inputs are not correct data types")
        except ValueError as e:
            raise ValueError("Description inputs are correctly typed but not"
                             "allowed")

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, in_desc):
        if in_desc is not None and in_desc is not "":
            if in_desc[0] is "*" or "\n" in in_desc:
                raise ValueError("Segment description cannot contain * or \\n")
        self._description = in_desc

    def __str__(self):
        """Gives the string formatted output of the class.

        Returns:
            [lat],[long],[alt],[description]
            or
            [lat],[long],[alt]
        """
        desc_str = Waypoint.__str__(self)
        if self._description is not "":
            desc_str += ","
        return '{}{}'.format(desc_str, self._description)

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
