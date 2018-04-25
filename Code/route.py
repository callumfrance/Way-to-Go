"""route.py"""
import re
from segment import Segment

class Route(Segment):
    """
    A route is a collection of joined waypoints with descriptions.

    Attributes:
        waypoints: a linked list of 'Waypoint' (long, lat, alt)
            that represent the path
        r_name: the name of the route (only contains [a-zA-Z0-9_])
        r_desc: the route description (cannot contan a newline character)
    """
    def __init__(self, r_desc, r_name):
        self.waypoints = list()
        self.route_desc = r_desc
        self.r_name = r_name

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
        return self.route_desc

    @route_desc.setter
    def route_desc(self, in_route_desc):
        """route description does not allow the newline character"""
        if "\n" in in_route_desc:
            raise ValueError("Description cannot contain newline")
        else:
            self.route_desc = in_route_desc

    def add_waypoint(self, in_waypoint, pos=None):
        """adds a waypoint to the route object"""
        if pos is not None:
            self.waypoints.insert(pos, in_waypoint)
        else:
            self.waypoints.append(in_waypoint)

    def retrieve_waypoint(self, pos):
        """retrieves a waypoint at a specified point along the route"""
        return self.waypoints[pos]
