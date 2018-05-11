import data
import threading
import time

class GpsLocator:
    def __init__(self):
        self.supervisor()

    def supervisor(self):
        x = threading.Thread(target=self.calc_location,
                             args=(,))
        x.start()
        # execute other code while thread is working
        # thread exit condition reached here
        x.join()

    def calc_location(self):
        y = data.gps_location_updates.split(" ")
        for y_one_line in y:
            line_lat = float(y_one_line[0])
            line_long = float(y_one_line[1])
            line_alt = float(y_one_line[2])

            self.locationReceived(line_lat, line_long, line_alt)

    @abstractmethod
    def locationReceived(latitude, longitude, altitude):
        pass
