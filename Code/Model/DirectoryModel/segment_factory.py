from .route import Route
from .description import Description


class SegmentFactory:

    def __init__(self):
        self.test_loader = None

    def set_test_loader(self, t1):
        """Allows test values to be passed through this factory."""
        self.test_loader = t1

    def make_all_data(self, data):
        """The only public method - makes populate route_dictionary.

        Parameters:
            data : String
                A string of a predetermined formatting, containing all
                the information required on all (global) Route data.

        Returns:
            new_directory : dict<Route>
                A populated dictionary of Routes containing segments.
        """
        if self.test_loader is not None:
            new_directory = self.test_loader
        else:
            data_lines = data.split("\n")
            new_routes = self._make_all_routes(data_lines)
            new_directory = self._make_all_segments(new_routes, data_lines)
        return new_directory

    def _make_all_routes(self, data_lines):
        """Iterates through entire data input and creates all Route objects."""
        route_dict = dict()
        for x in data_lines:
            """Iterate through every line in the data"""
            x = x.strip()
            y = x.split(",")
            if " " in y[0]:
                """Identified a line to be a Route"""
                x = x.split(" ")
                route_dict[x[0]] = self._make_route(x)
                print("\nRoute key " + x[0] + " value " + str(route_dict[x[0]]))
        return route_dict

    def _make_all_segments(self, route_dict, data_lines):
        """Iterate through entire input data and make a directory.

        Parameters:
            route_dict : dict<Route>

            data_lines : list<String>

        Return:
            route_dict : dict<Route>
                Route dictionary populated with all known Segments.
        """
        curr_route = None
        for x in data_lines:
            """Iterates through every line in the input data."""
            x = x.strip()
            y = x.split(",")
            if " " in y[0]:
                """Identified a line as a Route - update curr_route."""
                curr_route = (x.split(" "))[0]
            elif x != '':
                """Identified a line as not a Route."""
                new_seg = self._make_segment(x, route_dict)
                route_dict[curr_route].append_path(new_seg)
        return route_dict

    @staticmethod
    def _make_route(entry):
        """
        data_line : String
            "<route_name> <route_description>"
        """
        # entry = data_line.split(" ")
        new_route = Route(entry[0], entry[1])
        print("new route: " + str(new_route) + "\n")
        return new_route

    @staticmethod
    def _make_segment(data_line, route_dict):
        """
        data_line : String
            One of three forms:
                case 1 - "<float>,<float>,<float>,*<route_name>"
                or
                case 2 - "<float>,<float>,<float>,<description>"
                or
                case 3 - "<float>,<float>,<float>"
        """
        entry = data_line.split(",")
        entry[0] = float(entry[0])  # latitude
        entry[1] = float(entry[1])  # longitude
        entry[2] = float(entry[2])  # altitude

        if len(entry) is 3:
            """The data_line is the last one inside a given Route."""
            new_segment = Description(entry[0], entry[1], entry[2])
        elif entry[3][0] is '*':
            """The data_line references an already created Route (sub-route)."""
            desc_attr = ''.join(entry[3:])
            desc_attr = desc_attr[1:]            # Remove * from route name
            new_segment = route_dict[desc_attr]  # Retrieve Route
        else:
            """The data_line is a normal Description object."""
            desc_attr = ''.join(entry[3:])
            new_segment = Description(entry[0], entry[1], entry[2], desc_attr)

        print("new segment: " + str(new_segment) + "\n")
        return new_segment
