"""
Tracker

This class represents the data (i.e. model) pertaining to when the program
is in 'tracking' mode. It is a specific subset of data derived from the
DirectoryModel - it focuses on one Route, and the path along said route.

This object is only created during the tracking method in the Controller class,
and deleted at the end of that method - it is not designed to be a
permanent fixture in the program.
"""

# Author: Callum France

from ..DirectoryModel.waypoint import Waypoint
from ..DirectoryModel.description import Description
from ..DirectoryModel.route import Route
import sys
sys.path.append('../../')
from GpsLocator import GpsLocator
# GpsLocator is in the root folder so we must change the path to get access


class Tracker(GpsLocator):
    """The Tracker class.

    Attributes:
        self.the_route : Route
            The Route that the user is travelling along.

        self.curr_loc : Waypoint
            The current location of the user, according to GpsLocator.

        self.next_wp : Waypoint
            The next Waypoint the user should get to. This is derived from
            the_route, and can either be automatically or manually updated.

        self.remaining : list<float>
            This is the total horizontal distance, ascent, and descent the user
            must travel to reach the end, based on the distance between the
            user's current location and next_wp, and the distance from the
            next_wp to the last waypoint.

        self.tracker_change_obs : set<TrackerChangeObserver>
            This contains any observers that 'subscribe' to a change in Tracker
            info - particularly when the current location is updated or the
            next waypoint is manually updated.

        self._next_wp_position : int
            The integer position along the Route.gather_all_waypoints() list
            at which the next_wp resides.

        self._fin : Boolean
            True if the user has finished the_route and False otherwise.
    """

    def __init__(self, in_route):
        """Initialize the superclass GpsLocator (of which Tracker inherits),
        and then set the other Tracker properties.
        """
        GpsLocator.__init__(self)

        self._fin = False
        self._next_wp_position = 1
        self.the_route = in_route
        self.tracker_change_obs = set()
        self.curr_loc = (in_route.gather_all_waypoints())[0]
        self.next_wp = (in_route.gather_all_waypoints())[1]
        self.remaining = self._calc_total_distance()

    @property
    def curr_loc(self):
        return self._curr_loc

    @curr_loc.setter
    def curr_loc(self, in_curr_loc):
        """The mutator for the user's current location.

        When the current location is updated, a lot of other class fields must
        also be updated, as they are derived from this property.

        Must check if they have reached the end; if they have reached the
        next waypoint; Tracker must calculate the new remaining distances; and
        it must all let the observers know the class has been updated.
        """
        if isinstance(in_curr_loc, Waypoint):
            self._curr_loc = in_curr_loc
            # If other class attributes have not been created, don't do these
            if hasattr(self, 'next_wp') and hasattr(self, '_fin'):
                self.has_finished()
                self._close_enough()
                if not self._fin:
                    self._calc_remaining()
                self.notify_tracker_change_obs()

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
        """The 'remaining' mutator.

        If this array does not have a size analogous to [lat,long,alt], discard.
        """
        if isinstance(in_remaining, list):
            if len(in_remaining) is 3:
                self._remaining = in_remaining

    def _calc_total_distance(self):
        """Used to find the total distances for the route.

        Returns:
            dist: list<float>
                The total horizontal dist, alt, and desc for the_route.
        """
        dist = [
            self.the_route.find_distance(),
            self.the_route.find_ascent(),
            self.the_route.find_descent(),
        ]
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

        # Gathers all waypoints from the_route and any sub-routes
        all_points = self.the_route.gather_all_waypoints()

        # Iterate over all route waypoints and add totals.
        for x in range(self._next_wp_position, len(all_points)-1):
            cumulative[0] += all_points[x].calc_metres_dist(all_points[x+1])
            vert = all_points[x].calc_metres_vertical(all_points[x+1])
            cumulative[1] += vert[0]
            cumulative[2] += vert[1]

        # Must above total to distance between current loc and next_wp
        self.remaining[0] = cumulative[0] + \
            all_points[self._next_wp_position].calc_metres_dist(self.curr_loc)

        # Also for vertical distances
        vert = self.curr_loc.calc_metres_vertical(
            all_points[self._next_wp_position])
        self.remaining[1] = cumulative[1] + vert[0]
        self.remaining[2] = cumulative[2] + vert[1]

    def manually_complete_waypoint(self):
        """Called when a user indicates in UI they have reached the next_wp.
        _close_enough() must also update next_wp if user has reached their
        next waypoint, and so this method is called from there as well.

        Must tell all observers that Tracker has changed as a result.
        """
        self._next_wp_position += 1
        if not self.has_finished():
            self.next_wp = \
                (self.the_route.gather_all_waypoints())[self._next_wp_position]
        else:
            self.remaining = [0.0, 0.0, 0.0]
        self.notify_tracker_change_obs()

    def _close_enough(self):
        """Checks if the current location is within bounds to update
        the current waypoint.
        """
        if self.curr_loc.__eq__(self.next_wp):
            self.manually_complete_waypoint()

    def has_finished(self, manual_finish=False):
        """Checks if the user has reached the end of the Route.

        Attributes:
            manual_finish : Boolean
                This allows any other method, including a user input from UI
                to say that the Route has been finished (e.g. user gives up).

        Returns:
            self._fin : Boolean
                Returns the attribute that denotes if the Route has finished.
        """
        r_len = len(self.the_route.gather_all_waypoints())
        if manual_finish or self._next_wp_position >= r_len or \
                self.curr_loc.__eq__(
                (self.the_route.gather_all_waypoints()[r_len-1])):
            self._fin = True
        return self._fin

    def locationReceived(self, latitude, longitude, altitude):
        """Implementation of abstract class within GpsLocator.

        Simply calls the current location mutator, which does the rest.
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
        if isinstance(self.curr_loc, Description):
            self.curr_loc.description = ""
        out_string = ""
        out_string += "\tCurrent Location: " + self.curr_loc.__str__() + "\n"
        out_string += "\tNext Waypoint: " + self.next_wp.__str__() + "\n\t"
        out_string += "Remaining distance: " + str(round(self.remaining[0], 2))
        out_string += " m\n\tRemaining climb: "
        out_string += str(round(self.remaining[1], 2))
        out_string += " m\n\tRemaining descent: "
        out_string += str(round(self.remaining[2], 2)) + " m\n"
        return out_string

# -------------
# observer code
# -------------

    def add_tracker_change_ob(self, observer):
        """Adds a tracker observer to the set.

        Attributes:
            observer : TrackerChangeObserver
                A new observer to add to the set in this object.
        """
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
        """Will iterate through all observers and call relevant update code
        """
        for o in self.tracker_change_obs:
            """Give all observing class a reference to this Tracker object"""
            o.tracker_update(self)
