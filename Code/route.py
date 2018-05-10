"""
Route
"""
import re
from segment import Segment
from description import Description
from waypoint import Waypoint


class Route(Segment):
    """
    A route is a collection of joined waypoints with descriptions.

    Attributes:
        r_name: the name of the route (only contains [a-zA-Z0-9_])

        r_desc: the route description (cannot contain a newline character)

        pathway: a linked list of 'Segments'
            Represents the route path
    """
    def __init__(self, in_r_name, in_r_desc="", in_pathway=None):
        self.pathway = list()
        self.r_desc = in_r_desc
        self.r_name = in_r_name
        if in_pathway is not None:
            self.append_path(in_pathway)

    @property
    def r_name(self):
        """route name"""
        return self._r_name

    @r_name.setter
    def r_name(self, in_route_name):
        """route name mutator checks for valid characters"""
        pattern = r'[^\_a-zA-Z0-9]'
        if re.search(pattern, in_route_name):
            raise ValueError("Route name must only have:\ta-zA-Z0-9_")
        self._r_name = in_route_name

    @property
    def r_desc(self):
        """route description"""
        return self._r_desc

    @r_desc.setter
    def r_desc(self, in_route_desc):
        """route description does not allow the newline character"""
        if "\n" in in_route_desc:
            raise ValueError("Description cannot contain newline")
        self._r_desc = in_route_desc

    @property
    def pathway(self):
        return self._pathway

    @pathway.setter
    def pathway(self, val):
        self._pathway = val

    def append_path(self, in_seg):
        """Adds only one Segment to the end of pathway.

        If you try and add more than one item, it will call 'extend' instead.

        Parameters:
            in_seg : Segment

        Returns:
            A list of Segments representing the routes pathway.
        """
        if isinstance(in_seg, list):
            self.extend_path(in_seg)
        elif not self.valid_segment_check(in_seg):
            raise TypeError("Can only append Route/Description/Waypoint")
        else:
            self.pathway.append(in_seg)

    def extend_path(self, in_multi_segs):
        """Adds multiple pathways to the Route"""
        for x in in_multi_segs:
            if not self.valid_segment_check(x):
                raise TypeError("Can only extend Route/Description/Waypoint")
        self.pathway.extend(in_multi_segs)

    def retrieve_segment(self, pos):
        """Retrieves a segment at a specified point along the route."""
# This needs to be extended.
# In order for a new route to be created (case 2), it won't have any
# segments to begin with, but there needs to be 'something' there...
        return self.pathway[pos]

    @staticmethod
    def valid_segment_check(seg_to_check):
        """Static method to check if a segment is valid for the pathway.

        Parameters:
            seg_to_check : Object
                The object to validate - is it a Route, Description, or Waypoint

        Returns:
            is_valid : Boolean
                True only if seg_to_check is Route/Description/Waypoint
        """
        is_valid = False
        if isinstance(seg_to_check, (Description, Route, Waypoint)):
            is_valid = True
        return is_valid

# -----------------------------------------------------------------------------
# write a to_list() method to decrease coupling -
#     i.e. it will mean you dont have to recurse routes outside this class
#     too much
# -----------------------------------------------------------------------------

    def __str__(self):
        route_str = self.r_name + " " + self.r_desc
        for x in self.pathway:
            if isinstance(x, Route):
                route_str += "\n\t{},*{}".format(
                    x.pathway[0].__str__(), x.r_name)
            else:
                # route_str += "{}\n".format(x.__str())

                route_str += "\n\t{}".format(x.__str__())
        return route_str

    def calc_metres_dist(self, next_segment=None):
        """
        Selects two adjacent pathways and finds the distance between them.
        If the first pathway is actually a sub-route, it recursively
        finds that routes total distance, and adds that to this routes distance.
        Terminates at segments: 'seg' = length-1 and 'next_seg' = length

        Parameters:
            next_segment : Segment

        Returns:
            cumulative : float
        """
        cumulative = 0.0
        for i, seg in zip(range(len(self.pathway)-1), self.pathway):
            """
            Loops over all elements in pathway except the last one.
            Using zip with the length of 'pathway-1' terminates the
            loops last 'segment' early - there is no 'next' at that point
            """
            next_seg = self.pathway[i+1]
            if isinstance(seg, Route):
                """
                if seg is a Route, recurse and find that Routes distance
                """
                cumulative += seg.calc_metres_dist(None)
            else:
                """
                if next_seg is a Route, find its 1st waypoint
                """
                if isinstance(next_seg, Route):
                    x = next_seg.pathway[0]
                else:
                    x = next_seg
                cumulative += seg.calc_metres_dist(x)

        # Because float values are inprecise, rounding is necessary
        cumulative = round(cumulative, 2)
        return cumulative

    def calc_metres_vertical(self, next_segment=None):
        """Determines vertical climb and descent.

        Parameters:
            next_segment : Segment

        Returns:
            cumulative : float[2]
                cumulative[0] is the total climb distance in metres
                cumulative[1] is the total descent distance in metres
        """
        cumulative = [0.0, 0.0]
        for i, seg in zip(range(len(self.pathway)-1), self.pathway):
            """
             Loops over all elements in pathway except the last one.
             Using zip with the length of 'pathway-1' terminates the
             loops last 'segment' early - there is no 'next' at that point
             """
            next_seg = self.retrieve_segment(i+1)
            if isinstance(seg, Route):
                """
                if seg is a Route, recurse and find that Routes distance
                """
                subr_tot = seg.calc_metres_vertical(None)
                cumulative[0] += subr_tot[0]
                cumulative[1] += subr_tot[1]
                y = seg.retrieve_segment(len(seg.pathway)-1)
            else:
                y = seg

            if isinstance(next_seg, Route):
                x = next_seg.retrieve_segment(0)
            else:
                x = next_seg

            seg_vert = y.calc_metres_vertical(x)
            cumulative[0] += seg_vert[0]
            cumulative[1] += seg_vert[1]

        # Because float values are inprecise, rounding is necessary
        cumulative[0] = round(cumulative[0], 2)
        cumulative[1] = round(cumulative[1], 2)
        return cumulative

