from abc import ABC, abstractmethod
"""Segment.py"""
class Segment(ABC):
    def __init__(self, in_waypoints, in_description):
        self.waypoints = list()
        self.set_waypoints(in_waypoints)
        self.__description = description

    @property
    def description(self):
        return self.__description

    @description.setter
    def description(self, in_description):
        """Checks if description has any invalid characters."""
        if "\n" in in_description:
            raise Exception("Invalid description")
        self.description = in_description


    # --------
    # MUTATORS
    # --------
    def set_waypoints(self, in_waypoints):
        """Adds new waypoints."""
        # validate for entire range of 'waypoints'
        self.waypoints.append(in_waypoints)

    # ---------
    # ACCESSORS
    # ---------
    def get_waypoints(self):
        """Returns waypoints."""
        return self.waypoints
