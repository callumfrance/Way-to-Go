# Way-to-Go

Assumptions
-----------
- That GpsLocator.py and GpsLocator class is name as such (as opposed to GPSLocator)
- That GpsLocator.py and GeoUtils will be placed in the root directory of the program (i.e. directly inside the Code/ folder)
- That GpsLocator.locationReceived() has the added parameter of 'self', since it is not a static method.
- GpsLocator.locationRecieved() is not called _location_received() as you would expect a private method using PEP8, nor does is used name wrangling i.e. __locationReceived()
