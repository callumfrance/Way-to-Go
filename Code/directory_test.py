"""
directory_test.py
"""

# Author: Callum France

import unittest
from directory import Directory
from route import Route
from description import Description

class DirectoryTest(unittest.TestCase):
    """Test harness for the Directory class."""

    def setUp(self):
        """Always construct a blank directory before each test."""
        self.direct = Directory()

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
