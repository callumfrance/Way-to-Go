"""
Data

Contains data the GeoUtils stub imports into the Directory.
Also contains the data that the stub GpsLocator uses to get
fake location updates from.
"""

# Author: Callum France

# GeoUtils uses this data for retrieveRouteData()
test1 = "theClimb [description]\n \
\t-31.94,115.75,47.1,[description]\n \
\t-31.94,115.75,55.3,[description]\n \
\t-31.94,115.75,71.0,[description]\n \
\t-31.93,115.75,108.0,[description]\n \
\t-31.93,115.75,131.9\n \
mainRoute [description]\n \
\t-31.96,115.80,63.0,[description]\n \
\t-31.95,115.78,45.3,[description]\n \
\t-31.95,115.77,44.8,*theStroll\n \
\t-31.94,115.75,47.1,[description]\n \
\t-31.93,115.72,40.1,[description]\n \
\t-31.94,115.75,47.1,*theClimb\n \
\t-31.93,115.75,131.9,[description]\n \
\t-31.92,115.74,128.1\n \
theStroll [description]\n \
\t-31.95,115.77,44.8,[description]\n \
\t-31.93,115.76,43.0,[description]\n \
\t-31.94,115.75,47.1"


# Simulates walking along theStroll in GpsLocator stub
theStroll_location_updates = \
        "-31.95,115.77,44.8\n" \
        "-31.94932,115.76835,44.8\n" \
        "-31.947987,115.764623,44.0\n" \
        "-31.94254,115.7621,43.5\n" \
        "-31.93,115.76,43.0\n" \
        "-31.93261,115.75931,43.6\n" \
        "-31.9333,115.7573,45.03\n" \
        "-31.93799,115.75201,46.82\n" \
        "-31.94,115.75,47.1"

# Simulates walking along mainRoute in GpsLocator stub
mainRoute_location_updates = \
        "-31.96,115.80,63.0\n" \
        "-31.9552,115.7945,60.0\n" \
        "-31.95,115.78,45.3\n" \
        "-31.9503,115.7777,45.0\n" \
        "-31.95,115.77,44.8\n" \
        "-31.94901,115.7695,44.804\n" \
        "-31.94932,115.76835,44.8\n" \
        "-31.947987,115.764623,44.0\n" \
        "-31.94254,115.7621,43.5\n" \
        "-31.93,115.76,43.0\n" \
        "-31.93261,115.75931,43.6\n" \
        "-31.9333,115.7573,45.03\n" \
        "-31.93799,115.75201,46.82\n" \
        "-31.94,115.75,47.1\n" \
        "-31.94,115.75,47.1\n" \
        "-31.93,115.72,40.1\n" \
        "-31.939999,115.749999,46.1\n" \
        "-31.94,115.75,55.3\n" \
        "-31.94,115.75,71.0\n" \
        "-31.93,115.75,108.0\n" \
        "-31.93,115.75,131.9\n" \
        "-31.93,115.75,131.9\n" \
        "-31.92,115.74,128.1"

# Just outputs the data strings to the console for demonstration
if __name__ == '__main__':
    print("-------------------------")
    print("test1 is:\n\n{}".format(test1))
    print("-------------------------\n")
    print("\n-------------------------")
    print("theStroll_location_updates is:\n\n{}"
          .format(theStroll_location_updates))
    print("-------------------------")
    print("\n-------------------------")
    print("mainRoute_location_updates is:\n\n{}"
          .format(mainRoute_location_updates))
    print("-------------------------")

