from ..DirectoryModel.waypoint import Waypoint
from ..DirectoryModel.route import Route
import sys
sys.path.append('../../')
from GpsLocator import GpsLocator
# GpsLocator is in the root folder so we must change the path to get access


class Tracker(GpsLocator):
    """

    Attributes:
        self.the_route : Route

        self.curr_loc : Waypoint

        self.next_wp : Waypoint

        self.remaining : list<float>

        self.tracker_change_obs : set<TrackerChangeObserver>

        self._next_wp_position : int

        self._dist_up_to_next_wp : list<float>
    """

    def __init__(self, in_route):
        """Initialize the superclass GpsLocator (of which Tracker inherits)
        """
        GpsLocator.__init__(self)
        self.the_route = in_route
        self.curr_loc = (in_route.gather_all_waypoints())[0]
        self.next_wp = (in_route.gather_all_waypoints())[1]
        self._next_wp_position = 1
        self.remaining = self._calc_total_distance()
        self.tracker_change_obs = set()
        self._fin = False
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
            if in_curr_loc is not self.curr_loc:
                self._close_enough()
                self.has_finished()
                # update remaining
                # update dist_up_to_next_wp
                self.notify_tracker_change_obs()
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
            if in_next_wp is not self.next_wp:
                self._calc_remaining()
                self.notify_tracker_change_obs()
            self._next_wp = in_next_wp

    @property
    def remaining(self):
        return self._remaining

    @remaining.setter
    def remaining(self, in_remaining):
        if isinstance(in_remaining, list):
            if len(in_remaining) is 3:
                self._remaining = in_remaining

    def _calc_total_distance(self):
        dist = list()
        dist[0] = self.the_route.find_distance()
        dist[1] = self.the_route.find_ascent()
        dist[2] = self.the_route.find_descent()
        return dist

    def _calc_remaining(self):
        """Finds the remaining distance for the given route.

        Gathers all waypoint's from the Route into one list that can be iterated
        over.
        This allows a cumulative total to be formed from the next waypoint to
        the end of the route.
        Finally, the distance between the current location is added to this.
        """
        cumulative = [0.0, 0.0, 0.0]

        all_points = self.the_route.gather_all_waypoints()

        for x in range(self._next_wp_position, len(all_points)-1):
            cumulative[0] += all_points[x].calc_metres_dist(all_points[x+1])
            cumulative[1] += all_points[x].calc_metres_ascent(all_points[x+1])
            cumulative[2] += all_points[x].calc_metres_descent(all_points[x+1])

        self.remaining[0] = cumulative[0] + \
            all_points[self._next_wp_position].calc_metres_dist(self.curr_loc)
        self.remaining[1] = cumulative[1] + \
            all_points[self._next_wp_position].calc_metres_ascent(self.curr_loc)
        self.remaining[2] = cumulative[2] + \
            all_points[self._next_wp_position].calc_metres_descent(self.curr_loc)


    def _close_enough(self):
        """Checks if the current location is within bounds to update
        the current waypoint.
        """
        if self.curr_loc.__eq__(self.next_wp):
            self._next_wp_position += 1
            if self._next_wp_position is len(self.the_route.gather_all_waypoints()):
                self.has_finished(True)
            else:
                self.next_wp = self.the_route.retrieve_segment(self._next_wp_position)

    def has_finished(self, manual_finish=False):
        r_len = len(self.the_route.gather_all_waypoints())
        if manual_finish or self.curr_loc.__eq__(
                (self.the_route.gather_all_waypoints()[r_len-1])):
            self._fin = True
        return self._fin

    def locationReceived(self, latitude, longitude, altitude):
        """Implementation of abstract class within GpsLocator.
        """
        self.curr_loc = Waypoint(latitude, longitude, altitude)

    def __str__(self):
        """
        Returns:
            out_string : String
                "   Current location: <location>
                    Next Waypoint: <next_waypoint>
                    Remaining distance: <remaining[0]> m
                    Remaining ascent: <remaining[1]> m
                    Remaining descent: <remaining[2]> m
                "
        """
        out_string = ""
        out_string += "\tCurrent Location: " + self.curr_loc.__str__() + "\n"
        out_string += "\tNext Waypoint: " + self.next_wp.__str__() + "\n"
        out_string += "\tRemaining distance: " + self.remaining[0] + " m\n"
        out_string += "\tRemaining climb: " + self.remaining[1] + " m\n"
        out_string += "\tRemaining descent: " + self.remaining[2] + " m\n"
        return out_string

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
