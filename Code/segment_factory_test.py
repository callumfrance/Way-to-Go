"""
segment_factory_test.py
"""

# Author: Callum France

from segment_factory import SegmentFactory
import unittest
import data


class SegmentFactoryTest(unittest.TestCase):

    def setUp(self):
       self.seg_fact = SegmentFactory()

    # def test_make_route(self):
    #     r1 = SegmentFactory._make_route("")
    #     self.assertEquals(r1.__str__(), """answer""")

    # def test_make_segment(self):
    #     s1 = SegmentFactory._make_segment("")
    #     self.assertEquals(s1.__str__(), """answer""")

    # def make_all_routes(self):
    #     pass

    # def make_all_segments(self):
    #     pass

    def test_make_all_data(self):
        print("test_make_all_data: \n")
        test_dict_1 = self.seg_fact.make_all_data(data.test1)
        print("hello" + str(test_dict_1))


if __name__ == '__main__':
    unittest.main()

# Run the following in the shell:
#    python segment_factory_test.py -v
