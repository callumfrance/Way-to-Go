"""
Description
"""

# Author: Callum France

from segment import Segment
from waypoint import Waypoint


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
        except ValueError as e:
            raise ValueError
        except TypeError as e:
            raise TypeError
        self.description = in_desc

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, in_desc):
        if in_desc[0] is "*" or "\n" in in_desc:
            raise ValueError("Segment description cannot contain * or \\n")
        self._description = in_desc

    def __str__(self):
        """
        [lat],[long],[alt],[description]
        or
        [lat],[long],[alt]
        """
        desc_str = Waypoint.__str__(self)
        if self._description is not "":
            desc_str += ","
        return '{}{}'.format(desc_str, self._description)

# must be implemented
    def calc_metres_dist(self):
# list(3)
        pass

