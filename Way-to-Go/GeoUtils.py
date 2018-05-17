"""
GeoUtils

A stub used in order to implement Way-to-Go
"""

# Author: Callum France

from math import radians, sin, cos, acos
import data


# Naming according to the Assignment sheet does not use PEP8 - suppress warning
# noinspection PyPep8Naming
class GeoUtils(object):
    """GeoUtils.

    This class is a stub designed to implement several key facets
    used by Way-to-Go.
    """

    # noinspection PyPep8Naming
    @staticmethod
    def retrieveRouteData():
        """Inserts raw route data into program.

        Returns
        -------
        data.test1 : String
            One string representing all data for all routes.
        """
        return data.test1

    @staticmethod
    def calcMetresDistance(lat1, long1, lat2, long2):
        """Rough calculation of distance on Earth between two coordinates.

        Attributes
        ----------
        lat1 : float
            First point's latitude coordinate.

        long1 : float
            First point's longitude coordinate.

        lat2 : float
            Second point's latitude coordinate.

        long2 : float
            Second point's longitude coordinate.

        Returns
        -------
        final_z : float
            The calculated distance (in metres) between the two points.
        """
        part_a = sin(radians(lat1))
        part_b = sin(radians(lat2))
        part_c = cos(radians(lat1))
        part_d = cos(radians(lat2))
        part_e = cos(radians(abs(long1 - long2)))

        sum_x = acos(part_a*part_b + part_c*part_d*part_e)
        final_z = 6371000 * sum_x
        return final_z
