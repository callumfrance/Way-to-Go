from math import radians, sin, cos, cosh
import data

class GeoUtils(object):
    def retrieveRouteData():
        return data.test1

    def calcMetresDistance(lat1, long1, lat2, long2):
        a = sin(radians(lat1))
        b = sin(radians(lat2))
        c = cos(radians(lat1))
        d = cos(radians(lat2))
        e = cos(radians(abs(long1 - long2)))

        x = cosh(a*b + c*d*e)
        z = 6371000 * x
