"""
This is the abstract class representing the observer called when
the Directory is updated. This class is aggregated inside the Directory class
as a set. The class is inherited from (i.e. its concrete implementation)
inside the UI - in an inner nested class called DirUpdateObserverImpl.
"""

# Author: Callum France

import abc


class DirUpdateObserver(metaclass=abc.ABCMeta):

    def __init__(self):
        self.route_dict = None
        self.observer_state = None

    @abc.abstractmethod
    def dir_update(self, arg):
        """Implemented in the concrete observer class.
        """
        pass
