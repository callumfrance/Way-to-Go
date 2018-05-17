Way-to-Go Design Report
=======================
### Author: Callum France
##### Architectural Pattern
Way-to-Go used the model-view-controller architectural pattern.

Way-to-Go's model includes all information the program uses, and all calculations performed on said information. This is further separated into two sub-sections, the DirectoryModel, and the TrackerModel. The reason two sub-models were used is because some parts of the model are instantiated when the program begins, and some are created and destroyed during the course of the program. The program will always need to have one Directory object representing all known data in the program (DirectoryModel), however, when it enters tracking mode, it will need to create a sub-set of the known information and perform specialized calculations on them (TrackerModel).

Way-to-Go's view is simply the user interface. In this case, the view is console-based, simply outputting lines to the console, and reading inputs from the user.

The programs controller links the model to the view, and will call methods within itself when the programs changes state.

##### Composite Pattern
Way-to-Go uses the composite pattern to store route information. Because a it is possible for a route to contain a route, and then that route also contain a route, and so on, it was necessary to use a composite pattern to allow this kind of 'object recursion' to take place.
It was decided that along a routes pathway, each point could either represent another route, or a description with coordinates. Thus, the interface Segment was created in the UML, of which both Description and Route inherited from. Description was the leaf node (and also inherited from the base coordinate class Waypoint), and Route was the branch class, both inheriting and aggregating from Segment.
In this instance, the root level class in the composite pattern was always going to be a Route, and as such Directory simply inherits from Route instead of Segment.
It should also be worth noting that since Way-to-Go was written in Python, duck-typing has been used instead of writing a Segment class.

##### Dependency Injector Pattern
The Directory class uses a factory to create its map of routes in `update_directory()`. If this method was to create its own factory class directly, it would be incredibly hard to test the Directory class in isolation of SegmentFactory. Thus, dependency injection was included - the method instead has a SegmentFactory parameter, and Directory's parent class Controller creates the SegmentFactory object and passes it into `update_directory()`.
This increases testability of the code because you can now mock SegmentFactory when testing this method - otherwise the test code will create a fully functional SegmentFactory.

##### Factory Pattern
The Directory class needs to populate itself with information from GeoUtils, however this is a rather long and complicated process. Instead of including this functionality inside Directory, greatly increasing the length of the file and reducing its readability, the SegmentFactory class was created.
This factory has the sole purpose of reading in data from GeoUtils and outputting a map (in Python, a dictionary) of populated routes, accessed via their route name.
This means that in the future, if SegmentFactory or GeoUtils were changed, the Directory class is unscathed.

##### Iterator Pattern
Way-to-Go has a lot of lists, dictionaries, and sets. Often, the program needs to access all elements stored inside these data structures and perform an operation on each of them. Using the iterator pattern means that an operation can be performed on all elements, one at a time. For instance, when the Tracker class needs to update its observer, the iterator pattern for-loop is used to go through all elements in the tracker change set -

```python
def notify_tracker_change_obs(self):
	for o in self.tracker_change_obs:
		o.tracker_update(self)
```

##### Observer Pattern
The observer pattern allows the program to update itself in response to a certain event or action.
In Way-to-Go, two different observers are implemented - after the Directory has finished being updated; and after an 'accessible' class field in Tracker has changed.

By using an observer for Directory updates, it allows the view to display the updated information without resorting to some kind of polling in Controller. Instead, the DirectoryModel communicates directly to the View with an observer containing the updated information, allowing the display to instantly update.
Simarly, Tracker also provides an observer containing the updated information to the View to allow an update.

The concrete observers are nested classes inside appropriate View methods. This is because the observer implementations are only used in very specific and small sections of the UI. The concrete observers are created and added to their appropriate Model observer sets when the UI method begins, and removed when the method finishes. This is to prevent future Directory updates from erroneously overriding the current console display because it notified the UI directory observer.

##### Template Pattern
Way-to-Go uses the abstract hook method `GpsLocator.locationReceived()` to update the current location in Tracker. This is achieved by allowing Tracker to inherit from GpsLocator and writing the concrete hook method - which updates Trackers current location.
