"""
description_test
"""

# Author: Callum France

import unittest
from description import Description


class DescriptionTestCase(unittest.TestCase):
    """Test harness for the Description Class."""

    def setUp(self):
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
        desc_c = Description(33.3, 44.4, 55.5, "A morose mountain")
        print("\nFinished test_constructor()\n")

    def test_calc_metres_dist(self):
        """Checks the accuracy and validity of horizontal distance math."""
        desc_c = Description(33.3, 44.4, 55.5, "A morose mountain")
        val_1 = desc_c.calc_metres_dist(self.desc_b)
        self.assertEqual(round(val_1, 1), 3931835.1)
        val_2 = desc_c.calc_metres_dist(desc_c)
        self.assertEqual(round(val_2, 1), 0.0)
        val_3 = self.desc_b.calc_metres_dist(desc_c)
        self.assertEqual(round(val_3, 1), 3931835.1)
        self.assertEqual(val_3, val_1)
        val_4 = self.desc_b.calc_metres_dist(self.desc_b)
        self.assertEqual(round(val_4, 1), 0.0)
        print("\nFinished test_calc_metres_dist()\n")

    def test_calc_metres_vertical(self):
        """Checks the accuracy and validity of climb/descent distance math."""
        desc_c = Description(33.3, 44.4, 55.5, "A morose mountain")
        val_1 = desc_c.calc_metres_vertical(self.desc_b)
        self.assertEqual(round(val_1[0], 1), 0.0)
        self.assertEqual(round(val_1[1], 1), 41.1)
        val_2 = self.desc_b.calc_metres_vertical(desc_c)
        self.assertEqual(round(val_2[0], 1), 41.1)
        self.assertEqual(round(val_2[1], 1), 0.0)
        val_3 = self.desc_b.calc_metres_vertical(self.desc_b)
        self.assertEqual(round(val_3[0], 1), 0.0)
        self.assertEqual(round(val_3[1], 1), 0.0)
        print("\nFinished test_calc_metres_vertical()\n")


if __name__ == '__main__':
    unittest.main()

# Run the following in the shell:
#    python description_test.py -v
