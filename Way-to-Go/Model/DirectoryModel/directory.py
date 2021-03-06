"""
Directory

Contains an observer that allows you to subscribe to a 'whole Directory' change
        The view needs to know when the data changes so it can refresh
"""

# Author: Callum France


class Directory:
    """The contents of the entire model i.e. all the routes.

    Attributes:
        route_dict : dictionary of Routes
            A map of all the known routes.
            The key is each routes name.

        dir_wide_update_obs : set of observers
            The collection of observers that want to know when an update
            is made to the Directory
    """

    def __init__(self):
        """Constructor class

        Initializes the dictionary and sets
        """
        self.route_dict = dict()  # a dictionary of all recorded routes
        self.dir_wide_update_obs = set()

    # ------------------
    # functionality code
    # ------------------
    def update_directory(self, in_data, in_seg_fact):
        """Segment factory is a parameter because this utilizes
        dependency injection, and makes the code more testable.
        """
        seg_fact = in_seg_fact
        self.route_dict = seg_fact.make_all_data(in_data)
        self._notify_dir_wide_update_obs()

    def retrieve_route_data(self, in_r_name):
        """The accessor method for an individual Route in the Directory.

        Parameters:
            in_r_name : String
                The name of the Route that must be retrieved from Directory

        Returns:
            out_route : Route
                The requested Route object
        """
        # print(in_r_name)
        out_route = self.route_dict[in_r_name]
        return out_route

    def __str__(self):
        """Turns all relevant data in this Class into a String for the UI.

        Needs to display each routes -
            Name and description
            Beginning
            End
            Total distance
            Total ascent
            Total descent

        Returns:
            out_string : String
                The representation of this class in human-readable string form.
        """
        out_string = ""
        counter = 1
        for key, value in self.route_dict.items():
            out_string += key + " " + value.r_desc + "\n"
            out_string += "\t" + str(value.retrieve_segment(0)) + "\n\t"
            out_string += str(value.retrieve_segment(len(value.pathway)-1))
            out_string += "\n\t distance: "
            out_string += str(value.calc_metres_dist()) + " m\n"
            out_string += "\t ascent:" + str(value.find_ascent()) + " m\n"
            out_string += "\t descent: " + str(value.find_descent()) + " m\n"
            out_string += "\n\n"
            counter += 1
        if counter is 1:
            out_string += "You do not know any routes\n\n"
        return out_string

# -------------
# observer code
# -------------

    def add_dir_wide_update_ob(self, observer):
        """Adds a new observer to the set of observers.
        """
        self.dir_wide_update_obs.add(observer)

    def rem_dir_wide_update_ob(self, observer):
        """Will remove observer from set only if it was present.
        Will do nothing if observer was never in there.
        (use .remove() instead if an error needs to be raised)
        """
        try:
            self.dir_wide_update_obs.discard(observer)
        except IndexError:
            # Tried to remove an observer that was never in the Directory
            pass

    def _notify_dir_wide_update_obs(self):
        """Will iterate through all observers and call relevant update code.
        """
        for o in self.dir_wide_update_obs:
            o.update(self.route_dict)
