Design Report
=============
### Author: Callum France

Design patterns used:
- Architectural pattern
	- Model-View-Controller
		- Separates concerns
- Observer pattern
	- DirectoryUpdateObserver
		- Allows the view to update on dir event
	- TrackerChangeObserver
		- Allows view to update on tracker change
- Template pattern
	- GpsLocator
		- Hook method is Tracker allows separation of GPS logic from my programs logic
	- Observers use template
		- Allows each concrete observer to perform their own specific change when triggered.
- Composite pattern
	- Segment, Route, Description
		- Allows Routes to easily contain other Routes
- Iterator pattern
	 - for x in y:
		- Easily go through each element in datatype
- Factory pattern
	- SegmentFactory
		- Allows construction of segments to be decoupled from the directories implementation.
- Dependency Injector Pattern
	- SegmentFactory is injected into Directory
		- Increases testability of Directory - you can now Mock the SegmentFactory instead of Directory automatically creating a real one
