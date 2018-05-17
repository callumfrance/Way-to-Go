import abc


class TrackerChangeObserver(metaclass=abc.ABCMeta):

    def __init__(self):
        self.tracking = None
        self.observer_state = None

    @abc.abstractmethod
    def tracker_update(self, arg):
        """Implemented in the concrete observer class."""
        pass
