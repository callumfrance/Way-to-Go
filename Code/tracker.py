class Tracker(RouteInfo):

    def __init__(self):
        RouteInfo.__init__()
        self.location
        self.next_waypoint


"""
Tracking <Route Name>
    Current location: <location>
    Remaining:
        <h distance>
        <climb>
        <descent>
    Next Waypoint: <next_waypoint>

    'c' - manually complete this waypoint
    'e' - exit session early
"""
