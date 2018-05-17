from route import Route
from description import Description
from waypoint import Waypoint


class SegmentFactory:

    def make_segment(self, data_line):
        """Make either a description/waypoint or route based on format.
        in_data : String
            One of four forms:
                case 1 - "<route_name> <route_description>"
                or
                case 2 - "<float>,<float>,<float>,*<route_name>"
                or
                case 3 - "<float>,<float>,<float>,<description>"
                or
                case 4 - "<float>,<float>,<float>"
        """
        seg = None

        x = data_line.split(",")

        if " " in x[0]:
            """case 1
            Must check if the route already exists first.
            """
            seg = Route(x[0], x[1:])
            y = data_line.split(" ", 1)  # splits into two strings by the space
        else:
            try:
                x[0] = float(x[0])
                x[1] = float(x[1])
                x[2] = float(x[2])
            except TypeError as e:
                raise TypeError("Must begin with 3 float coordinates")
            if x[3] is None:
                """case 4"""
                seg = Waypoint(x[0], x[1], x[2])
            elif x[3][1] is not "*":
                """case 3"""
                seg = Description(x[0], x[1], x[2], x[3])
            else:
                """case 2
                Must check if the route already exists first.
                """
                seg = Route(x[3][1:], "")

        return seg

    def make_route(self, data_line):
        """
        Ideally this should be refactored so that make_segment() calls
        make_route() instead of make_route() calling make_segment()

        Parameters:
            data_line : String
                A line representing a route.
                At this point in time, should only be of the format -
                case 1 - "<route_name> <route_description>"

                However in the future it could also take case 2

        Returns:
            new_route_obj : Route
        """
        new_route_obj = self.make_segment(data_line)
        if not isinstance(new_route_obj, Route):
            raise TypeError("A new Route should always be a Route object...")
        return new_route_obj
