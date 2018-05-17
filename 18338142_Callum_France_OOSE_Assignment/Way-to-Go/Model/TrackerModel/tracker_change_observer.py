"""
This is the abstract class representing the observer called when
the Tracker is changed. This class is aggregated inside the Tracker class
as a set. The class is inherited from (i.e. its concrete implementation)
inside the UI - in an inner nested class called TrackerChangeObserverImpl.
"""

# Author: Callum France

import abc


class TrackerChangeObserver(metaclass=abc.ABCMeta):

    def __init__(self):
        self.tracking = None
        self.observer_state = None

    @abc.abstractmethod
    def tracker_update(self, arg):
        """Implemented in the concrete observer class."""
        pass
