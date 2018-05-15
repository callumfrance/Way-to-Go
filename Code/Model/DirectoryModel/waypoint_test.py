"""
waypoint_test

navigate to the root directory of this project in the console
Run the following in the console
      python -m Model.DirectoryModel.waypoint_test
"""

# Author: Callum France

import unittest
from .waypoint import Waypoint


class WaypointTestCase(unittest.TestCase):
    """Test harness for the Waypoint Class."""

    def setUp(self):
        self.wp_a = Waypoint(33.3, 44.4, 55.5)

    def test_constructor(self):
        """Check constructor validity"""
        with self.assertRaises(TypeError):
            wp_b = Waypoint("grasp", 12.5, 0.01)
            print("wp_b is: {}".format(wp_b))
        with self.assertRaises(TypeError):
            wp_b = Waypoint(45.5, "gorilla", -10.21)
            print("wp_b is: {}".format(wp_b))
        with self.assertRaises(TypeError):
            wp_b = Waypoint(45.5, 175.2, "lion")
            print("wp_b is: {}".format(wp_b))

    def test_set_latitude(self):
        """Checks latitude validity."""
        with self.assertRaises(TypeError):
            self.wp_a.latitude = 131
            print(self.wp_a)
        with self.assertRaises(ValueError):
            self.wp_a.latitude = -90.01
            print(self.wp_a)
        with self.assertRaises(TypeError):
            self.wp_a.latitude = "elephant"
            print(self.wp_a)
        self.wp_a.latitude = -88.0
        self.assertEqual(self.wp_a.latitude, -88.0)

    def test_set_longitude(self):
        """Checks longitude validity."""
        with self.assertRaises(ValueError):
            self.wp_a.longitude = 180.01
        with self.assertRaises(TypeError):
            self.wp_a.longitude = -300
        with self.assertRaises(TypeError):
            self.wp_a.longitude = "giraffe"
        self.wp_a.longitude = 0.0
        self.assertEqual(self.wp_a.longitude, 0)
        self.wp_a.longitude = -108.0
        self.assertEqual(self.wp_a.longitude, -108.0)

    def test_set_altitude(self):
        """Checks altitude validity."""
        with self.assertRaises(TypeError):
            self.wp_a.altitude = "hello world"
            print(self.wp_a)
        self.wp_a.altitude = -10000.0
        self.assertEqual(self.wp_a.altitude, -10000.0)
        self.wp_a.altitude = 5123.43
        self.assertEqual(self.wp_a.altitude, 5123.43)

    def test_waypoint(self):
        """Tests that a waypoint is correctly constructed."""
        self.assertEqual(self.wp_a.latitude, 33.3)
        self.assertEqual(self.wp_a.longitude, 44.4)
        self.assertEqual(self.wp_a.altitude, 55.5)

    def test_eq(self):
        """Tests that two waypoints are close enough to be the same."""
        # Two idential waypoints
        self.assertTrue(self.wp_a.__eq__(Waypoint(33.3, 44.4, 55.5)))

        # Two slightly non-identical waypoints horizontally
        self.assertTrue(self.wp_a.__eq__(Waypoint(33.30008, 44.4, 55.5)))

        # Two slightly non-identical waypoints horizontally
        self.assertTrue(self.wp_a.__eq__(Waypoint(33.3, 44.40009, 55.5)))

        # Two slightly non-identical waypoints vertically
        self.assertTrue(self.wp_a.__eq__(Waypoint(33.3, 44.4, 57.5)))

        # Two slightly non-identical waypoints vertically
        self.assertTrue(self.wp_a.__eq__(Waypoint(33.3, 44.4, 53.5)))

        # Two slightly non-idential waypoints
        self.assertTrue(self.wp_a.__eq__(Waypoint(33.30003, 44.40004, 56.5)))

        self.assertFalse(self.wp_a.__eq__(Waypoint(33.301, 44.4, 55.5)))
        self.assertFalse(self.wp_a.__eq__(Waypoint(33.3, 44.401, 55.5)))
        self.assertFalse(self.wp_a.__eq__(Waypoint(33.3, 44.401, 57.6)))


if __name__ == '__main__':
    unittest.main()

# navigate to the root directory of this project in the console
# Run the following in the console
#       python -m Model.DirectoryModel.waypoint_test
