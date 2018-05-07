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

    def __init__(self):
        self.route_list = dict()  # a dictionary of all recorded routes
        self.dir_wide_update_obs = set()
        self.single_route_retrieval_obs = set()

# ------------------
# functionality code
# ------------------

    def update_directory(self, in_data):
        """
        calls the segment factory to create objects using input.
        then notifies all dir_wide_update_obs

        might also need to create another factory just to create routes
        """
        line_by_line = in_data.splitline()
        for line in line_by_line:
           """call the factory to make segments"""

    def retrieve_route_data(self, in_r_name):
        """
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

# -------------
# observer code
# -------------

    def add_dir_wide_update_ob(self, observer):
        self.dir_wide_update_obs.add(observer)

    def rem_dir_wide_update_ob(self, observer):
        """Will remove observer from set only if it was present.
        Will do nothing if observer was never in there.
        ( use .remove() instead if an error needs to be raised)
        """
        self.dir_wide_update_obs.discard(observer)

    def notify_dir_wide_update_obs(self):
        for o in self.dir_wide_update_obs:
            o.update("""stuff to do with Concrete observer""")

    def add_single_route_retrieval_ob(self, observer):
        self.single_route_retrieval_obs.add(observer)

    def rem_single_route_retrieval_ob(self, observer):
        """Will remove observer from set only if it was present.
        Will do nothing if observer was never in there.
        ( use .remove() instead if an error needs to be raised)
        """
        self.single_route_retrieval_obs.discard(observer)

    def notify_single_route_retrieval_obs(self):
        for o in self.single_route_retrieval_obs:
            o.update("""stuff to do with Concrete observer""")

