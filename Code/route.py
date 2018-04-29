"""route.py"""
import re
from segment import Segment
from waypoint import Waypoint


class Route(Segment):
    """
    A route is a collection of joined waypoints with descriptions.

    Attributes:
        waypoints: a linked list of 'Waypoint' (long, lat, alt)
            that represent the path
        r_name: the name of the route (only contains [a-zA-Z0-9_])
        r_desc: the route description (cannot contan a newline character)
    """
    def __init__(self, r_name, r_desc, in_waypoints=None):
        self.waypoints = list()
        self.route_desc = r_desc
        self.r_name = r_name
        if in_waypoints is not None:
            self.add_waypoints(in_waypoints)

    @property
    def r_name(self):
        """route name"""
        return self.r_name

    @r_name.setter
    def r_name(self, in_route_name):
        """route name mutator checks for valid characters"""
        pattern = r'[^\_a-zA-Z0-9]'
        if re.search(pattern, in_route_name):
            raise ValueError("Route name must only have:\ta-zA-Z0-9_")
        else:
            self.r_name = in_route_name

    @property
    def route_desc(self):
        """route description"""
        return self._route_desc

    @route_desc.setter
    def route_desc(self, in_route_desc):
        """route description does not allow the newline character"""
        if "\n" in in_route_desc:
            raise ValueError("Description cannot contain newline")
        else:
            self.route_desc = in_route_desc

    def add_waypoints(self, in_waypoints):
        """Iterates 'add_waypoint' to add a list full of waypoints."""
        if in_waypoints is list:
            for x in in_waypoints:
                self.add_waypoint(x)
        else:
            raise TypeError("Multiple waypoints should be a 'list' data type")

    def add_waypoint(self, in_waypoint=None,
                     in_lat=None, in_long=None, in_alt=None, pos=None):
        """adds a waypoint to the route object"""
        if in_waypoint is None or not isinstance(in_waypoint, Waypoint):
            if in_lat is None or in_long is None or in_alt is None \
                    or not isinstance(in_lat, float) \
                    or not isinstance(in_long, float) \
                    or not isinstance(in_alt, float):
                raise TypeError("Either waypoint object, or its attributes")
            else:
                in_waypoint = Waypoint(in_lat, in_long, in_alt)
        if pos is not None:
            self.waypoints.insert(pos, in_waypoint)
        else:
            self.waypoints.append(in_waypoint)

    def retrieve_waypoint(self, pos):
        """retrieves a waypoint at a specified point along the route"""
        return self.waypoints[pos]

# must be implemented
    def calc_metres_dist(self):
        pass
