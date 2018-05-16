import sys
from GeoUtils import GeoUtils

# sys.path.append('../')

from Model.DirectoryModel import Directory
from Model.DirectoryModel import SegmentFactory
from Model.TrackerModel import Tracker
from View.UI import UI

__author__ = 'Callum France'


class Controller:
    def __init__(self):
        self.view = UI()
        self.directory_model = Directory()
        self.seg_fact = SegmentFactory()

    def main_menu(self):
        selected_exit = False
        while not selected_exit:
            choice = self.view.main_menu_wrapper(self.directory_model)
            if choice is 1:
                # user wants to update the routes
                self.update_routes()
            elif choice is 2:
                # user wants to exit the program
                selected_exit = True
            else:
                # user has selected a route by entering its name
                self.route_selected(choice)
        print("\n")

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
        track = Tracker(chosen_route)
        print("created track in controller")
        self.view.tracking_wrapper(track)
        del track
