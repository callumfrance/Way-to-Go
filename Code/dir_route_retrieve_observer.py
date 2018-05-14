import abc


class DirRouteRetrieveObserver(metaclass=abc.ABCMeta):

    def __init__(self):
        self.route = None
        self.observer_state = None

    @abc.abstractmethod
    def dir_update(self, arg):
        pass