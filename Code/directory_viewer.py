from rdata_observer import RouteDataObserver

class DirectoryViewer:
    """Contains the concrete directory observer"""

    # Directory d

    # def setup():
    #     """Sets up the inner class observer."""
    #     d.addObserver(RouteDataObserver())

    # class DirectoryObserverImpl(RouteDataObserver):
    #     """The inner class observer"""

    #     def update_directory():
    #         """Implementation of RouteDataObserver abstract method."""


    """
    Implement the Observer updating interface to keep its state
    consistent with the subjects.
    Store state that should stay consistent with the subjects
    """

    def update(self, arg):
        self._observer_state = arg
        """add things here"""
