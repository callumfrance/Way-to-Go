Way-to-Go
=========
#### by Callum France
2018


Running
-------
1. Install Python 3 (3.6) on your machine
2. Navigate to the Way-to-Go/ folder
3. Execute `python main.py`

## Running a test unit
1. Install Python 3 on your machine
2. Navigate to the Way-to-Go/ folder
3. Execute `python -m <Package>.<file_name>` e.g. `python -m Model.DirectoryModel.route_test`


Assumptions
-----------
- That GpsLocator.py and GpsLocator class is named as such (as opposed to GPSLocator or gps_locator)
- That GeoUtils.py is named as such (as opposed to geo_utils.py)
- That GpsLocator.py and GeoUtils.py will be placed in the root directory of the program (i.e. directly inside the Way-to-Go/ folder)
- That GpsLocator.locationReceived() has the added parameter of 'self', since it is not a static method.
- `GpsLocator.locationRecieved()` is not called `_location_received()` as you would expect a private method using PEP8, nor does is used name wrangling i.e. `__locationReceived()`
