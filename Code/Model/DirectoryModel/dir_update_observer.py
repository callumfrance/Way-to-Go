import abc


class DirUpdateObserver(metaclass=abc.ABCMeta):

    def __init__(self):
        self.route_dict = None
        self.observer_state = None

    @abc.abstractmethod
    def dir_update(self, arg):
        """Implemented in the concrete observer class."""
        pass
