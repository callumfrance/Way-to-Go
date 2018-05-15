from ..DirectoryModel.waypoint import Waypoint
from ..DirectoryModel.route import Route
import sys

# GpsLocator is in the root folder so we must change the path to get access
sys.path.append('../../')

from GpsLocator import GpsLocator


class Tracker(GpsLocator):
    """
    Tracking <Route Name>
        Current location: <location>
        Remaining:
            <h distance>
            <climb>
            <descent>
        Next Waypoint: <next_waypoint>

        'c' - manually complete this waypoint
        'e' - exit session early
    """

    def __init__(self, in_route):
        """Initialize the superclass GpsLocator (of which Tracker inherits)
        """
        GpsLocator.__init__(self)
        self.the_route = in_route
        self.curr_loc = in_route.retrieve_segment(0)
        self.next_wp = in_route.retrieve_segment(1)
        self.remaining = self.calc_remaining(self.curr_loc) #must write this

    @property
    def curr_loc(self):
        return self._curr_loc

    @curr_loc.setter
    def curr_loc(self, in_curr_loc):
        if isinstance(in_curr_loc, Waypoint):
            self.curr_loc = in_curr_loc

    @property
    def the_route(self):
        return self._the_route

    @the_route.setter
    def the_route(self, in_route):
        if isinstance(in_route, Route):
            self._the_route = in_route

    @property
    def next_wp(self):
        return self._next_wp

    @next_wp.setter
    def next_wp(self, in_next_wp):
        if isinstance(in_next_wp, Waypoint):
            self._next_wp = in_next_wp

    @property
    def remaining(self):
        return self._remaining

    @remaining.setter
    def remaining(self, in_remaining):
        if isinstance(in_remaining, list):
            if len(in_remaining) is 3:
                self._remaining = in_remaining

    def __str__(self):
        out_string = ""
        out_string += "\tCurrent Location: " + self.curr_loc.__str__() + "\n"
        out_string += "\tNext Waypoint: " + self.next_wp.__str__() + "\n"
        out_string += "\tRemaining distance: " + self.remaining[0] + " m\n"
        out_string += "\tRemaining climb: " + self.remaining[1] + " m\n"
        out_string += "\tRemaining descent: " + self.remaining[2] + " m\n"
        return out_string

    def __calc_remaining(self):
        """Finds the remaining distance for the given route
        """
        pass

    def __close_enough(self):
        """Checks if the current location is within bounds to update
        the current waypoint.
        """
        pass

    def locationReceived(self, in_lat, in_long, in_alt):
        """Implementation of abstract class within GpsLocator.
        """
        pass
