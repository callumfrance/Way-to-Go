"""
waypoint_test

Author: Callum France
"""
import unittest
from waypoint import Waypoint


class WaypointTestCase(unittest.TestCase):
    """Test harness for the Waypoint Class."""

    def setUp(self):
        self.wp_a = Waypoint(33.3, 44.4, 55.5)

    def test_set_latitude(self):
        """Checks latitude validity."""
        with self.assertRaises(ValueError):
            self.wp_a.latitude = 131
        with self.assertRaises(ValueError):
            self.wp_a.latitude = -90.01
        with self.assertRaises(ValueError):
            self.wp_a.latitude = "elephant"
        print(self.wp_a.latitude)
        self.wp_a.latitude = -88.0
        self.assertEqual(self.wp_a.latitude, -88.0)
        print(self.wp_a.latitude)

    def test_set_longitude(self):
        """Checks longitude validity."""
        with self.assertRaises(ValueError):
            self.wp_a.longitude = 180.01
        with self.assertRaises(ValueError):
            self.wp_a.longitude = -300
        with self.assertRaises(ValueError):
            self.wp_a.longitude = "giraffe"
        print(self.wp_a.longitude)
        self.wp_a.longitude = 0.0
        self.assertEqual(self.wp_a.longitude, 0)
        print(self.wp_a.longitude)
        self.wp_a.longitude = -108.0
        self.assertEqual(self.wp_a.longitude, -108.0)
        print(self.wp_a.longitude)

    def test_set_altitude(self):
        """Checks altitude validity."""
        with self.assertRaises(ValueError):
            self.wp_a.altitude = "hello world"
        print(self.wp_a.altitude)
        self.wp_a.altitude = -10000.0
        self.assertEqual(self.wp_a.altitude, -10000.0)
        print(self.wp_a.altitude)
        self.wp_a.altitude = 5123.43
        self.assertEqual(self.wp_a.altitude, 5123.43)
        print(self.wp_a.altitude)

    def test_waypoint(self):
        """Tests that a waypoint is correctly constructed."""
        self.assertEqual(self.wp_a.latitude, 33.3)
        self.assertEqual(self.wp_a.longitude, 44.4)
        self.assertEqual(self.wp_a.altitude, 55.5)
        print(self.wp_a.latitude,
              self.wp_a.longitude,
              self.wp_a.altitude)


if __name__ == '__main__':
    unittest.main()

# Run the following in the shell:
#    python waypoint_test.py -v
