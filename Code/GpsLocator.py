import abc
import data
import threading

"""
This class is a stub for the real GpsLocator.

It is designed to read in test data
    i.e. data.theStroll_location_updates
and then call the abstract hook method locationReceived() every 4 seconds.
"""

__author__ = 'Callum France'


class GpsLocator(metaclass=abc.ABCMeta):

    def __init__(self):
        """
        Sets up a new timer thread
        Connects to the GPS reader hardware
            (i.e. the data stub file)
        Calls the hook whenever it receives new coordinates
            (i.e. every 4 seconds)

        Attributes:
            _gps_data : list<list<float>>
                A list of all the coordinates from the test data - each of
                which are a list of 3 floats representing lat, long, and alt.

            _current_pos : int
                A 'current position marker' which represents the point along the
                test data the user is currently supposed to be at.
        """
        self._gps_data = list()
        self._construct_data(data.theStroll_location_updates)
        self._current_pos = -1
        self.t = None
        self._time_function()

    def _time_function(self):
        """Simulates time spent walking between two spots on a pathway."""
        self._current_pos += 1
        self._location_received_wrapper(self._gps_data[self._current_pos])
        if self._current_pos < len(self._gps_data):
            """Only keep going if you have not reached the end of the walk."""
            self.t = threading.Timer(1, self._time_function)
            self.t.start()

    def _construct_data(self, in_str):
        """Takes in the input data and formats it into _gps_data as a list
        of lists. Each list-list contains three coordinates - lat, long, alt
        """
        lines = in_str.split("\n")
        for x in lines:
            y = list()
            x_coords = x.split(",")
            for single_coord in x_coords:
                y.append(float(single_coord))
            self._gps_data.append(y)

    def _location_received_wrapper(self, coords):
        """Expand list(3) into three floats to pass to abstact method."""
        # print("locationReceived coords are: " + str(coords) + "\n")
        self.locationReceived(coords[0], coords[1], coords[2])

    def __del__(self):
        print("called GpsLocator delete")
        self.t.cancel()
        self.t.join()

    @abc.abstractmethod
    def locationReceived(self, latitude, longitude, altitude):
        pass
