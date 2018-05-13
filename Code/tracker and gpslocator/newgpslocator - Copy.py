import data
import time

class GpsLocator:
    def __init__(self):
        self.calc_location()

    def calc_location(self):
        y = data.theStroll_location_updates.split("\n")
        for y_one_line in y:
            coords = y_one_line.split(",")
            line_lat = float(y_one_line[0])
            line_long = float(y_one_line[1])
            line_alt = float(y_one_line[2])
            self.locationReceived(line_lat, line_long, line_alt)
            time.sleep(5)

    @abstractmethod
    def locationReceived(latitude, longitude, altitude):
        pass
