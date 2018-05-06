from description import Description
from route import Route

class SegmentFactory:
    def make_segment(data_line):
        """Make either a description or route based on format.
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
            """case 1"""
            seg = Route(x[0], x[1:])
            y = data_line.split(" ", 1) # splits into two strings by the space
        else:
            try:
                x[0] = float(x[0])
                x[1] = float(x[1])
                x[2] = float(x[2])
            except:
                raise TypeError("Must begin with 3 float coordinates")
            if x[3] is None
                """case 4"""
                seg = Description(x[0], x[1], x[2])
            elif x[3][1] is not "*":
                """case 3"""
                seg = Description(x[0], x[1], x[2], x[3])
            else:
                """case 2"""
                seg = Route(x[3][1:], "")

        return seg
