"""Segment.py"""
class Segment():
    """
    def abstract_method(self):
        raise NotImplementedError
    """

    def __init__(self, in_waypoints, in_description):
        self.waypoints = list()
        self.set_waypoints(in_waypoints)
        self.set_description(in_description)

    # --------
    # MUTATORS
    # --------
    def set_description(self, in_description):
        """Checks if description has any invalid characters."""
        if "\n" in in_description:
            raise Exception("Invalid description")
        self.description = in_description

    def set_waypoints(self, in_waypoints):
        """Adds new waypoints."""
        # validate for entire range of 'waypoints'
        self.waypoints.append(in_waypoints)

    # ---------
    # ACCESSORS
    # ---------
    def get_description(self):
        """Returns description."""
        return self.description

    def get_waypoints(self):
        """Returns waypoints."""
        return self.waypoints
