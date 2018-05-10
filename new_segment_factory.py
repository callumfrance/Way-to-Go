from route import Route
from description import Description
from waypoint import Waypoint


class SegmentFactory:

    def make_all_segments(self, data):
        """Iterates througn entire data input and creates all Segments."""
        pass

    def make_segment(self, data_line):
        pass

    def make_all_routes(self, data):
        """Iterates through entire data input and creates all Route objects."""
        route_dict = dict()
        data_line = data.split("\n")
        for x in data_line:
            x = x.strip()
            y.split(",")
            if " " in y[0]:
                route_dict[x[0]] = self.make_route(x)
        return route_dict

    def make_route(self, data_line):
        """
        data_line : String
            "<route_name> <route_description>"
        """
        entry = data_line.split(" ")
        try:
            new_route = Route(entry[0], entry[1])
        except TypeError e:
            pass
        return new_route


















    def make_segment(self, data_line):
        """Make either a description/waypoint or route based on format.
        data_line : String
            One of three forms:
                case 1 - "<float>,<float>,<float>,*<route_name>"
                or
                case 2 - "<float>,<float>,<float>,<description>"
                or
                case 3 - "<float>,<float>,<float>"
        """
        entry = data_line.split(",")
        entry[0] = float(entry[0])
        entry[1] = float(entry[1])
        entry[2] = float(entry[2])

        if len(entry) is 3:
            """The data_line is the last one inside a given Route."""
            new_segment = Description(entry[0], entry[1]
        elif entry[3][0] is "*":
            """The data_line is a sub-route"""
            self.make_route(data_line)
        else:
            """The data_line is a Description object"""
            new_segment = Description(entry[0], entry[1], entry[2], "END")

        return new_segment
