from GeoUtils import GeoUtils
from directory import Directory
from segment_factory import SegmentFactory
from tracker import Tracker
from UI import UI


class Controller():
    def __init__(self):
        self.view = UI()
        self.directory_model = Directory()
        self.seg_fact = SegmentFactory()
        # self.tracker_model = Tracker()
        # tracker model requires an input route...

    def main_menu(self):
        selected_exit = False
        while not selected_exit:
            choice = self.view.main_menu_wrapper(self.directory_model)
            if choice is 'A':
                self.update_routes()
            elif choice is 'B':
                # exit
                selected_exit = True
            else:
                # user has selected a route
                self.route_selected(choice)

    def update_routes(self):
        in_data = GeoUtils.retrieveRouteData()
        self.directory_model.update_directory(in_data, self.seg_fact)

    def route_selected(self, route_val):
        chosen_route = self.directory_model.retrieve_route_data(route_val)
        choice = self.view.display_one_route(chosen_route)
        if choice is 1:
            # begin the route tracking
            self.tracking(chosen_route)

    def tracking(self, chosen_route):
        pass
