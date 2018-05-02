"""
description_test
"""

# Author: Callum France
import unittest
from description import Description


class DescriptionTestCase(unittest.TestCase):
    """Test harness for the Description Class."""

    def setUp(self):
        self.wp_y = (33.3, 44.4, 55.5)
        self.wp_x = (-88.8, -77.7, -66.6)
        # self.desc_a = Description("A morose mountain.", self.wp_x)
        self.desc_b = Description(12.2, 13.3, 14.4, "A downhill disaster")

    def test_constructor(self):
        """Check constructor validity"""
        with self.assertRaises(ValueError):
            desc_c = Description(45.9, -39.3, 198.3, "*The plain plains")
            print("desc_c is: {}".format(desc_c))
        with self.assertRaises(ValueError):
            desc_c = Description(19.23, -40.9, 954.4, "New Day\nNew Me")
            print("desc_c is: {}".format(desc_c))
        with self.assertRaises(TypeError):
            desc_c = Description(53.2, -23.5, "The well liked hike", "nope")
            print("desc_c is: {}".format(desc_c))
        print("\nFinished test_constructor()\n")

    # def test_set_description(self):
    #     """Checks description validity."""


if __name__ == '__main__':
    unittest.main()

# Run the following in the shell:
#    python description_test.py -v