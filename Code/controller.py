from GeoUtils import retrieveRouteData
from directory import Directory
from tracker import Tracker
from UI import UI


class Controller():
    def __init__(self):
        self.view = UI()
        self.directory_model = Directory()
        # self.tracker_model = Tracker()
        # tracker model requires an input route...

    def main_menu(self):
        choice = self.view.display_main_menu()
        if choice is 'A':
            self.update_routes()
        elif choice is 'B':
            # exit
            pass
        else:
            # user has selected a route
            self.route_selected(choice)
            pass

    def update_routes(self):
        in_data = retrieveRouteData()
        self.directory_model.update_directory(in_data)

    def route_selected(self, route_val):
        chosen_route = self.directory_model.retrieve_route_data(route_val)
        choice = self.view.display_one_route(chosen_route)
        if choice is 1:
            # begin the route
            pass
        elif choice is 2:
            # go back to main
            self.main_menu()

    def tracking(self):
        pass
