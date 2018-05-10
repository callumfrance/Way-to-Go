from waypoint import Waypoint
from route import Route


class Tracker:
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

    def __init__(self, in_curr_loc, in_route):
        self.curr_loc = in_curr_loc
        self.the_route = in_route
        self.remaining = self.calc_remaining()
        self.next_wp = self.close_enough()

    @property
    def curr_loc(self):
        return self._curr_loc

    @property
    def the_route(self):
        return self._the_route

    @the_route.setter
    def the_route(self, in_route):

    @property
    def remaining(self):
        return self._remaining

    @property
    def next_wp(self):
        return self._next_wp

    def calc_remaining(self):
        """Finds the remaining distance for the given route
        """
        pass

    def close_enough(self):
        """Checks if the current location is within bounds to update
        the current waypoint.
        """
        pass

