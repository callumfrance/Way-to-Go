"""
Description
"""

# Author: Callum France

from segment import Segment
from waypoint import Waypoint


class Description(Segment):
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

        point : Waypoint
            The position along the route that this description applies to.
    """

    def __init__(self, in_desc="", in_waypoint=None,
                 in_lat=None, in_long=None, in_alt=None):
        self.description = in_desc
        try:
            self.point = in_waypoint
        except TypeError as e:
            try:
                self.point = Waypoint(in_lat, in_long, in_alt)
            except TypeError as e:
                raise TypeError("Invalid Description class parameters")
            except ValueError as e:
                raise ValueError("Invalid Description class parameters")

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, in_description):
        if in_description[0] is "*" or "\n" in in_description:
            raise ValueError("Segment description cannot contain * or \\n")
        else:
            self._description = in_description

    @property
    def point(self):
        return self._point

    def __str__(self):
        return '{},{}'.format(self._point, self._description)

# must be implemented
    def calc_metres_dist(self):
        pass

