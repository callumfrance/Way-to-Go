"""
Description
"""

# Author: Callum France

from segment import Segment


class Description(Segment):
    """
    A description is the leaf node in the Segment composite pattern.

    It is a segment that can not be represented by a route, but simply
    by a description.
    """

    def __init__(self, in_desc, in_waypoint=None,
                 in_lat=None, in_long=None, in_alt=None):
        self.description = in_desc
        self.waypoint

# must be implemented
    def calc_metres_dist(self):
        pass

    @property
    def description(self):
        return self._