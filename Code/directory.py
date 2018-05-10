"""
Two observers -
    One that allows you to subscribe to a 'whole Directory' change
        The view needs to know when the data changes so it can refresh
    One that allows you to see when a Route is retrieved from Directory
        Tracker will want to subscribe to this
        Once it has picked a route, it will unsubscribe
            This means more route calls can be made without 'restarting' tracker
        Once the Tracker has finished the route, it can resubscribe

"""


class Directory:
    """The contents of the entire model i.e. all the routes.

    Attributes:
        route_list : dictionary of Routes
            A map of all the known routes.
            The key is each routes name.

        dir_wide_update_obs : set of observers
            The collection of observers that want to know when an update
            is made to the Directory

        single_route_retrieval_obs : set of observers
            The collection of observers that want to know when a
            specific Route's information is accessed
    """

    def __init__(self):
        """Constructor class

        Initializes the dictionary and sets
        """
        self.route_list = dict()  # a dictionary of all recorded routes
        self.dir_wide_update_obs = set()
        self.single_route_retrieval_obs = set()

# ------------------
# functionality code
# ------------------

    def update_directory(self, in_data):
        """
        [INCOMPLETE]

        Calls the segment factory to create objects using input.
        then notifies all dir_wide_update_obs

        might also need to create another factory just to create routes
        """
        line_by_line = in_data.splitline()
        for line in line_by_line:
           """call the factory to make segments"""

    def retrieve_route_data(self, in_r_name):
        """The accessor method for an individual Route in the Directory.

        Parameters:
            in_r_name : String
                The name of the Route that must be retrieved from Directory

        Returns:
            out_route : Route
                The requested Route object
        """
        out_route = self.route_list[in_r_name]
        self.notify_single_route_retrieval_obs()
        return out_route

    def __str__(self):
        out_string = ""
        iter = 1
        for key, value in self.route_list.items():
            out_string += iter + ". " key + " " + value.r_desc + "\n"
            out_string += "\t" + value.retrieve_segment(0) + "\n"
            out_string += "\t" + value.retrieve_segment(len(value.pathway)-1)
            out_string += "\n\n"
            iter += 1
        return out_string

# -------------
# observer code
# -------------

    def add_dir_wide_update_ob(self, observer):
        """Adds a new observer to the set of observers"""
        self.dir_wide_update_obs.add(observer)

    def rem_dir_wide_update_ob(self, observer):
        """Will remove observer from set only if it was present.
        Will do nothing if observer was never in there.
        ( use .remove() instead if an error needs to be raised)
        """
        try:
            self.dir_wide_update_obs.discard(observer)
        except IndexError:
            # should I raise an issue?
            pass

    def notify_dir_wide_update_obs(self):
        """
        [INCOMPLETE]
        Will iterate through all observers and call relevant update code
        """
        for o in self.dir_wide_update_obs:
            o.update("""stuff to do with Concrete observer""")

    def add_single_route_retrieval_ob(self, observer):
        """Adds a new observer to the set of observers"""
        self.single_route_retrieval_obs.add(observer)

    def rem_single_route_retrieval_ob(self, observer):
        """Will remove observer from set only if it was present.
        Will do nothing if observer was never in there.
        ( use .remove() instead if an error needs to be raised)
        """
        try:
            self.single_route_retrieval_obs.discard(observer)
        except IndexError:
            # should I raise an issue?
            pass

    def notify_single_route_retrieval_obs(self):
        """
        [INCOMPLETE]

        Will iterate through all observers and call relevant update code
        """
        for o in self.single_route_retrieval_obs:
            o.update("""stuff to do with Concrete observer""")

