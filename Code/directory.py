"""RouteInfo.py"""
class Directory():

    def __init__(self):
        self._observers = set()
        self._route_list = {}

    @property
    def route_list(self):
        return self._route_list

    """"
    Other route_list methods here
    """

    def add_retrieve_rdata_observer(self, observer):
        observer._subject = self
        self._observers.add(observer)

    def remove_retrieve_rdata_observer(self, observer):
        observer._subject = None
        self._observers.discard(observer)

    def notify_observers(self):
        for observer in self._observers:
            observer.update(self._route_list)

    def add_route(in_route):
        pass
