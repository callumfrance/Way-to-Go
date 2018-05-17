"""
segment_factory_test.py

navigate to the root directory of this project in the console
Run the following in the console
      python -m Model.DirectoryModel.segment_factory_test
"""

# Author: Callum France

from .segment_factory import SegmentFactory
import unittest
import data  # contains the big input string given in the Assignment sheet


class SegmentFactoryTest(unittest.TestCase):

    def setUp(self):
        self.seg_fact = SegmentFactory()

    def test_make_all_data(self):
        print("test_make_all_data: \n")

        test_dict_1 = self.seg_fact.make_all_data(data.test1)
        # self.assertEquals(test_dict_1, """big fucking thing here""")
        print(str(test_dict_1))


if __name__ == '__main__':
    """Tells console to run this file as a unit test."""
    unittest.main()

# navigate to the root directory of this project in the console
# Run the following in the console
#       python -m Model.DirectoryModel.segment_factory_test
