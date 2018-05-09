"""
route_test.py
"""

# Author: Callum France
import unittest
from description import Description
from route import Route
from waypoint import Waypoint


class RouteTestCase(unittest.TestCase):
    """Test harness for the Route class"""

    def setUp(self):
        self.d1_1 = Description(-31.94, 115.75, 47.1, "d1_1 is hilly")
        self.d1_2 = Description(-31.94, 115.75, 55.3, "d1_2 is slippery")
        self.d1_3 = Description(-31.94, 115.75, 71.0, "d1_3 is rocky")
        self.d1_4 = Description(-31.93, 115.75, 108.0, "d1_4 is piney")
        self.wp_1 = Waypoint(-31.93, 115.74, 108.0)
        self.d2_1 = Description(-31.96, 115.80, 63.0, "d2_1 is loamy")
        self.d2_2 = Description(-31.95, 115.78, 45.3, "d2_2 is sandy")

    def test_r_desc(self):
        """Tests the route description"""
        r1 = Route("PassableName")
        self.assertEqual(r1.__str__(), "PassableName ")

        r2 = Route("1_More_Name", "Passable Description #33")
        self.assertEqual(r2.__str__(), "1_More_Name Passable Description #33")

        with self.assertRaises(TypeError):
            r6 = Route("Wanton_Winter", -12.3)
            print("Test failed: r6 is {}".format(r6.__str__()))

        r7 = Route("Scorching_Summer", "*Scorching_Summer")
        self.assertEqual(r7.__str__(), "Scorching_Summer *Scorching_Summer")

        r1.r_desc = "haha new route description"
        self.assertEqual(r1.__str__(),
                         "PassableName haha new route description")

    def test_r_name(self):
        """Tests the route name string"""
        r1 = Route("PassableName")
        self.assertEqual(r1.__str__(), "PassableName ")

        r2 = Route("1_More_Name", "Passable Description #33")
        self.assertEqual(r2.__str__(), "1_More_Name Passable Description #33")

        with self.assertRaises(ValueError):
            r3 = Route("Oopsie Woopsie", "A good description")
            print("Test failed: r3 is {}".format(r3.__str__()))

        with self.assertRaises(ValueError):
            r4 = Route("*Woopsie", "A good description")
            print("Test failed: r4 is {}".format(r4.__str__()))

        with self.assertRaises(TypeError):
            r5 = Route(6, "A good description")
            print("Test failed: r5 is {}".format(r5.__str__()))

        r7 = Route("Scorching_Summer", "*Scorching_Summer")
        self.assertEqual(r7.__str__(), "Scorching_Summer *Scorching_Summer")

        r2.r_name = "NewNameR2"
        self.assertEqual(r2.__str__(), "NewNameR2 Passable Description #33")

    def test_add_pathway(self):
        r1 = Route("Scorching_Summer", "A hot one!", self.d1_1)
        self.assertEqual(r1.__str__(), "Scorching_Summer A hot one!\n\t"
                                       "-31.94,115.75,47.1,d1_1 is hilly")

        r1.append_path(self.d1_2)
        self.assertEqual(r1.__str__(), "Scorching_Summer A hot one!\n\t"
                                       "-31.94,115.75,47.1,d1_1 is hilly\n\t"
                                       "-31.94,115.75,55.3,d1_2 is slippery")

        with self.assertRaises(TypeError):
            r1.append_path(100)
            print(r1.__str__())

        r1.append_path(self.wp_1)
        self.assertEqual(r1.__str__(), "Scorching_Summer A hot one!\n\t"
                                       "-31.94,115.75,47.1,d1_1 is hilly\n\t"
                                       "-31.94,115.75,55.3,d1_2 is slippery\n\t"
                                       "-31.93,115.74,108.0")

# should it fail if you try to append after a Waypoint?

    def test_add_pathways(self):
        """Tests adding multiple Segments to self.pathway"""
        r1 = Route("Scorching_Summer", "A hot one!")
        r1.extend_path([self.d1_1, self.d1_2, self.d1_3])
        self.assertEqual(r1.__str__(), "Scorching_Summer A hot one!\n\t"
                                       "-31.94,115.75,47.1,d1_1 is hilly\n\t"
                                       "-31.94,115.75,55.3,d1_2 is slippery\n\t"
                                       "-31.94,115.75,71.0,d1_3 is rocky")
        del r1

        r1 = Route("Scorching_Summer", "A hot one!")
        r1.append_path([self.d1_1, self.d1_2, self.d1_3])
        self.assertEqual(r1.__str__(), "Scorching_Summer A hot one!\n\t"
                                       "-31.94,115.75,47.1,d1_1 is hilly\n\t"
                                       "-31.94,115.75,55.3,d1_2 is slippery\n\t"
                                       "-31.94,115.75,71.0,d1_3 is rocky")

# also add a Route to a Route

    def test_calc_dist(self):
        """Tests the calc_metres_dist() algorithm"""
        r1 = Route("Scorching_Summer", "A hot one!")
        r1.extend_path([self.d1_1, self.d1_2, self.d1_3, self.wp_1])

        self.assertEqual(r1.calc_metres_dist(), """the answer""")

# also do an example of a route within a route

    def test_calc_vert(self):
        """Tests the calc_metres_vertical() algorithm"""
        r1 = Route("Scorching_Summer", "A hot one!")
        r1.extend_path([self.d1_1, self.d1_2, self.d1_3, self.wp_1])

        self.assertEqual(r1.calc_metres_vertical(), """the answer""")

# also do an example of a route within a route



if __name__ == '__main__':
    unittest.main()

# Run the following in the shell:
#    python route_test.py -v
