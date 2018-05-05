"""
route_test.py
"""

# Author: Callum France
import unittest
from route import Route
from waypoint import Waypoint


class RouteTestCase(unittest.TestCase):
    """Test harness for the Route class"""

    def setUp(self):
        self.d1_1 = Description(-31.94,115.75,47.1,"d1_1 is hilly")
        self.d1_2 = Description(-31.94,115.75,55.3,"d1_2 is slopey")
        self.d1_3 = Description(-31.94,115.75,71.0,"d1_3 is rocky")
        self.d1_4 = Description(-31.93,115.75,108.0,"d1_4 is piney")
        self.d2_1 = Description(-31.96,115.80,63.0,"d2_1 is loamy")
        self.d2_2 = Description(-31.95,115.78,45.3,"d2_2 is sandy")

    def test_r_desc(self):
        """Tests the route description"""
        pass

    def test_r_name(self):
        """Tests the route name string"""
        pass

    def test_add_pathway(self):
        """Tests adding one Segment to self.pathway"""
        pass

    def test_add_pathways(self):
        """Tests adding multiple Segments to self.pathway"""
        pass

    def test_calc_dist(self):
        """Tests the calc_metres_dist() algorithm"""
        pass

    def test_calc_vert(self):
        """Tests the calc_metres_vertical() algorithm"""
        pass

if __name__ == '__main__':
    unittest.main()

# Run the following in the shell:
#    python route_test.py -v
