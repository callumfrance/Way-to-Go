"""
directory_test.py
"""

# Author: Callum France

import unittest
from directory import Directory
from route import Route
from description import Description
from segment_factory import SegmentFactory


class DirectoryTest(unittest.TestCase):
    """Test harness for the Directory class."""

    def setUp(self):
        """Always construct a blank directory before each test."""
        d1_1 = Description(-31.94, 115.75, 47.1, "d1_1 is hilly")
        d1_2 = Description(-31.94, 115.75, 55.3, "d1_2 is slippery")
        d1_3 = Description(-31.94, 115.75, 71.0, "d1_3 is rocky")
        d2_1 = Description(-31.96, 115.80, 63.0, "d2_1 is loamy")
        d2_2 = Description(-31.95, 115.78, 45.3, "d2_2 is sandy")

        r1 = Route("TestName", "Great choice", [d2_1, d2_2,])
        r2 = Route("TestName", "Great choice", [d1_1, d1_2, d1_3,])
        factory_in_1 = {r1.r_name: r1, }
        factory_in_2 = {r1.r_name: r1, r2.r_name: r2, }
        self.fact_1 = SegmentFactory()
        self.fact_2 = SegmentFactory()
        self.fact_1.set_test_loader(factory_in_1)
        self.fact_2.set_test_loader(factory_in_2)

        self.direct = Directory()

    def tearDown(self):
        del self.fact_1
        del self.fact_2
        del self.direct

    def test_update_directory(self):
        pass

    def test_retrieve_route_data(self):
        pass

    def test_dir_wide_update_obs(self):
        pass

    def test_single_route_retrieval_obs(self):
        pass


if __name__ == '__main__':
    unittest.main()

# Run the following in the shell:
#    python directory_test.py -v
