from ..DirectoryModel.waypoint import Waypoint
from ..DirectoryModel.route import Route
import sys
sys.path.append('../../')
from GpsLocator import GpsLocator
# GpsLocator is in the root folder so we must change the path to get access


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
        self._next_wp_position = 1
        self.remaining = self._calc_total_distance()
        self.tracker_change_obs = set()
        self._dist_up_to_next_wp = [
                self.curr_loc.calc_metres_dist(self.next_wp),
                self.curr_loc.calc_metres_ascent(self.next_wp),
                self.curr_loc.calc_metres_descent(self.next_wp),
            ]

    @property
    def curr_loc(self):
        return self._curr_loc

    @curr_loc.setter
    def curr_loc(self, in_curr_loc):
        if isinstance(in_curr_loc, Waypoint):
            self._curr_loc = in_curr_loc

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

    def _calc_total_distance(self):
        dist = list()
        dist[0] = self.the_route.find_distance()
        dist[1] = self.the_route.find_ascent()
        dist[2] = self.the_route.find_descent()
        return dist

    def _calc_remaining(self):
        """Finds the remaining distance for the given route
        """
        pass

    def __close_enough(self):
        """Checks if the current location is within bounds to update
        the current waypoint.
        """
        if self.curr_loc.__eq__(self.next_wp):
            self._next_wp_position += 1
            if self._next_wp_position is len(self.the_route.gather_all_waypoints()):
                # it has reached the end of the route!
                pass
            else:
                self.next_wp = self.the_route.retrieve_segment(self._next_wp_position)
                self._calc_remaining()
                self.notify_tracker_change_obs()

    def has_finished(self):
        pass

    def locationReceived(self, in_lat, in_long, in_alt):
        """Implementation of abstract class within GpsLocator.
        """
        pass

# -------------
# observer code
# -------------

    def add_tracker_change_ob(self, observer):
        self.tracker_change_obs.add(observer)

    def rem_tracker_change_ob(self, observer):
        """Will remove observer from set only if it was present.
        Will do nothing if observer was never in there.
        (use .remove() instead if an error needs to be raised)
        """
        try:
            self.tracker_change_obs.discard(observer)
        except IndexError:
            # should I raise an issue?
            pass

    def notify_tracker_change_obs(self):
        """
        Will iterate through all observers and call relevant update code
        """
        for o in self.tracker_change_obs:
            """Give all observing class a reference to this Tracker object"""
            o.update(self)

