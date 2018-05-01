"""
description_test
"""

# Author: Callum France
import unittest
from description import Description
from waypoint import Waypoint

class DescriptionTestCase(unittest.TestCase):
    """Test harness for the Description Class."""

    def setUp(self):
        self.wp_y = (33.3, 44.4, 55.5)
        self.wp_x = (-88.8, -77.7, -66.6)
        self.desc_a = Description("A morose mountain.", self.wp_x)
        self.desc_b = Description("A downhill disaster", 12.2, 13.3, 14.4)

    def test_constructor(self):
        """Check constructor validity"""
        with self.assertRaises(ValueError):
            desc_c = Description("*The plain plains", self.wp_y)
            print("desc_c is: {}".format(desc_c))
        with self.assertRaises(ValueError):
            desc_c = Description("New Day\nNew Me", self.wp_y)
            print("desc_c is: {}".format(desc_c))
        with self.assertRaises(TypeError):
            desc_c = Description("The well liked hike", 53.2, -23.5)
            print("desc_c is: {}".format(desc_c))

    def test_set_description(self):
        """Checks description validity."""

if __name__ == "__main__"
    unittest.main()

# Run the following in the shell:
#    python waypoint_test.py -v