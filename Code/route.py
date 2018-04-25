import re
from segment import Segment

class Route(Segment):
    def __init__(self, r_desc, r_name):
        self.waypoints = list()
        self.route_desc = r_desc
        self.r_name = r_name

    @property
    def r_name(self):
        return self.r_name

    @r_name.setter
    def r_name(self, in_route_name):
        pattern = r'[^\_a-zA-Z0-9]'
        if re.search(pattern, in_route_name):
            raise ValueError("Route name must only have:\ta-zA-Z0-9_")
        else:
            self.r_name = in_route_name

    @property
    def route_desc(self):
        return self.route_desc

    @route_desc.setter
    def route_desc(self, in_route_desc):
        if "\n" in in_route_desc:
            raise ValueError("Description cannot contain newline")
        else:
            self.route_desc = in_route_desc

    def append_waypoint(self, in_waypoint):
        self.waypoints.append(in_waypoint)

    def insert_waypoint(self, in_waypoint, pos):
        self.waypoints.insert(pos, in_waypoint)

    def retrieve_waypoint(self, pos):
        return self.waypoints[pos]
