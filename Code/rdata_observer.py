import abc

class RouteDataObserver(metaclass=abc.ABCMeta):
    """An abstract observer class for when GeoUtils.retrieveRouteData()
    is called.

    Observer for the Directory class (model) and DirectoryViewer (view).
    """

    def __init__(self):
        self._directory = None
        self._observer_state = None

    @abc.abstractmethod
    def update_directory(self, arg):
        pass

