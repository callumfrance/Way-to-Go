"""
Joins the Model to the View and is the 'buffer' between the two.
Links all files in the program together.
"""

# Author: Callum France

import sys
from GeoUtils import GeoUtils
from Model.DirectoryModel import Directory
from Model.DirectoryModel import SegmentFactory
from Model.TrackerModel import Tracker
from View.UI import UI


class Controller:
    def __init__(self):
        self.view = UI()
        self.directory_model = Directory()
        self.seg_fact = SegmentFactory()

    def main_menu(self):
        """The main_menu is the point at which a user will begin and
        end the program, and everything in between.

        From here, the user can either exit the program, update routes,
        or select a route to view - each of which
        will call another method inside the Controller.
        """
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
        """Retrieves route data from GeoUtils and adds it to the Directory,
        which is then displayed on the main menu.
        """
        in_data = GeoUtils.retrieveRouteData()
        self.directory_model.update_directory(in_data, self.seg_fact)

    def route_selected(self, route_val):
        """Retrieves the selected route from the Directory and displays it
        to the single route view method in the UI. If the user does not choose
        this route this method will simply exit and return to the main_menu.

        Attributes:
            route_val : String
                This is the name of a route the user wishes to traverse down.
        """
        chosen_route = self.directory_model.retrieve_route_data(route_val)
        choice = self.view.display_one_route(chosen_route)
        if choice is 1:
            # begin the route tracking
            self.tracking(chosen_route)

    def tracking(self, chosen_route):
        """Links together a Tracker class and the UI tracking section
        for when a user wants to travel a Route.

        Parameters:
            chosen_route : Route
                This is the Route that the use has selected to travel along.
        """
        track = Tracker(chosen_route)
        self.view.tracking_wrapper(track)
        del track
