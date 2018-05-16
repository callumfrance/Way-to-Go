# ---------------
# WayToGoModel.py
# ---------------
from abc import ABC, abstractmethod
class WayToGoModel(ABC):
    def __init__(self):
        self.all_routes = list()
        # self.add_route_data()

    def add_route_data(self, in_data):
        """
        in_data : String
            Represents a single line of input data (i.e. a route segment).
            e.g.
            "-31.94,115.75,47.1,[description]"
            or
            "theClimb [description]"
        """
        new_thing = SegmentFactory(in_data.strip()) # strips whitespace
        self.all_routes.append(new_thing)
        """However, only want to append Routes to all_routes, and
        append Descriptions to within a route..."""

    @abstractmethod
    def make_segment(self):
        raise NotImplementedError("Implement this abstract class")

# -----------------
# SegmentFactory.py
# -----------------
class SegmentFactory(WayToGoModel):
    def make_segment(self, in_data):
        """Make either a description or route based on format.
        in_data : String
            One of three forms:
                "<float>,<float>,<float>,*<route_name>"
                or
                "<float>,<float>,<float>,<description>"
                or
                "<float>,<float>,<float>"
        """
        x = in_data.split(",")
        try:
            x[0] = float(x[0])
            x[1] = float(x[1])
            x[2] = float(x[2])
        except:
            raise TypeError("Input must begin with 3 float coordinates")
        if len(x) is not 3:
            if len(x) is not 2:
                raise TypeError("Input must have 2 or 3 fields")
            new_segment = Description(x[0], x[1], x[2])
        else:
            if x[3][0] is "*":
                new_segment = make_sub_route(x[3][1:], "")
            else:
                new_segment = Description(x[0], x[1], x[2], x[3])
        return new_segment


# -------------------
# BaseRouteFactory.py
# -------------------
class RouteFactory(WayToGoModel):
    def make_base_route(self, in_r_name, in_r_desc):
        """Makes a new route if it does not already exist."""
       route_found = False
        for y : WayToGoModel.all_routes:
            if y.r_name is in_r_name and not route_found:
                """The route already exists."""
                new_base_route = y
                route_found = True
        if not route_found:
            """Must create a new base route to return instead"""
            new_base_route = Route(in_r_name, in_r_desc)
        return new_base_route

    def make_sub_route(self, in_r_name, in_r_desc):
        """Makes a new sub route if it does not already exist.
        """
        return make_base_route(in_r_name, in_r_desc)

    # def does_route_exist(self, in_r_name, in_r_desc):
    #     route_exists = False
    #     for y : WayToGoModel.all_routes:
    #         if y.r_name is in_r_name and not route_exists:
    #             route_exists = True
    #     return route_exists
