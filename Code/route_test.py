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
        b_1 = [33.3, 44.4, 0.0]
        b_2 = [0.61, -12.2, 100.1]
        b_3 = [-6.66, -179.9, 124.3]
        b_point_list = list[b_1, b_2, b_3]
        self.route_a = Route("Hill Climb", "A long uphill")
        self.route_b = Route("Crit", "A cyclic bicycle route", b_point_list)

    def test_add_waypoint(self):
        self.route_a.add_waypoint(self.b_1)

    def test_add_waypoints(self):