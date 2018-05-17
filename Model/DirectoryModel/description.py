"""
Description
"""

# Author: Callum France

from .waypoint import Waypoint


class Description(Waypoint):
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
        except TypeError:
            raise TypeError("Description inputs are not correct data types")
        except ValueError:
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
