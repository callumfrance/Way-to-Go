from waypoint import Waypoint
from route import Route


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
        """Initiatialize the superclass GpsLocator (of which Tracker inherits)
        """
        GpsLocator.__init__()
        self.the_route = in_route
        self.curr_loc = in_route.retrieve_segment(0)
        self.next_wp = in_route.retrieve_segment(1)
        self.remaining = self.calc_remaining(curr_loc)

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

#     class DirRouteRetrieveObserverImpl(DirRouteRetrieveObserver):
#         """Concrete inner class representation of DirRouteRetrieveObserver
#         """
#
#         def update(self, arg):
#             """Updates tracker with the correct Route it is based on."""
#             self.the_route = arg
#             self.curr_loc = arg.retrieve_segment(0)
#             self.next_wp = arg.retrieve_segment(1)
#             self.remaining = self.calc_remaining(curr_loc)
#
#     def tear_down(self):
#         """Called when Tracker is no longer being used."""
#
