"""
UI

The class responsible for console output and user input.
"""

# Author: Callum France

import sys
import os
sys.path.append('../')
from Model.TrackerModel.tracker_change_observer import TrackerChangeObserver
from Model.DirectoryModel.dir_update_observer import DirUpdateObserver


class UI:
    """The original view class

    Attributes:
        There are no attributes for this view, so it can be instantiated
        without requiring any inputs.
    """

    @staticmethod
    def _clear_screen():
        """Simple static method to clear the console,
        to allow new info to be printed.
        """
        os.system('cls' if os.name == 'nt' else 'clear')

    def main_menu_wrapper(self, in_directory):
        """

        Attributes:
            in_directory : Directory
                The Directory to display to the console

        Return:
            choice : String or int
                Either a String representing the chosen Routes name,
                or
                an integer to exit program (2) or update routes (1)
        """
        class DirUpdateObserverImpl(DirUpdateObserver):
            """The concrete observer class for Directory updates in the UI.
            """
            def dir_update(self, arg):
                # Calls the main menu again with the new Directory fields.
                UI._display_main_menu(arg)

        concrete_dir_update_ob = DirUpdateObserverImpl()
        # add this newly created concrete observer to the Director ob set
        in_directory.add_dir_wide_update_ob(concrete_dir_update_ob)

        # static method that actually output info to the console
        choice = self._display_main_menu(in_directory)

        # remove observer from Director ob set to prevent erroneous calls
        in_directory.rem_dir_wide_update_ob(concrete_dir_update_ob)
        return choice

    @staticmethod
    def _display_main_menu(in_directory):
        """Display console output, and receives users choice

        Attributes:
            in_directory : Directory
                The Directory to display to the console

        Return:
            choice : String or int
                Either a String representing the chosen Routes name,
                or
                an integer to exit program (2) or update routes (1)
        """
        choice = 5  # set choice to something invalid to enter the while loop
        # Must check if user input matches any route name listed in the Dir
        pattern = list(in_directory.route_dict.keys())
        UI._clear_screen()

        # while choice is not A or B or any valid route_list number
        while choice not in pattern and choice is not 1 and choice is not 2:
            print("-----------------------------------------\n"
                  "- - - - - - - - Way-to-Go - - - - - - - -\n"
                  "-----------------------------------------\n\n")
            print("\t1. Update routes \n"
                  "\t2. Exit\n"
                  "\tor enter a route name for more detail\n\n")
            print("{}".format(in_directory.__str__()))
            choice = input("\n> ")
            UI._clear_screen()

            if choice not in pattern:
                try:
                    choice = int(choice)
                except ValueError:  # User simply not entered an integer.
                    pass  # Does not require any action
                if choice is not 1 and choice is not 2:
                    # User has not entered 1, 2, or a known Route name
                    print("Please select a valid route name, "
                          "update, or exit.\n")

        return choice

    @staticmethod
    def display_one_route(in_route):
        """Displays a Route and its segments.

        Used to determine if a user wants to 'go' on this route.

        Attributes:
            in_route : Route
                The route to display to the console.

        Returns:
            choice : int
                Exit (2) or begin tracking this route (1).
        """

        choice = 'F'  # set choice to something invalid to enter the while loop
        while choice != 1 and choice != 2:
            print("---------------------------------------------\n"
                  "- - - - - - - - Route View  - - - - - - - - -\n"
                  "---------------------------------------------\n\n")
            print("\t1. Begin route\n"
                  "\t2. Back\n\n")
            print("{}".format(in_route.__str__()))
            try:
                choice = int(input("\n> "))
            except ValueError:  # User simply not entered an integer.
                pass  # Does not require any action
            UI._clear_screen()
            if choice != 1 and choice != 2:
                # User has not entered a valid option
                print("\nPlease enter 1 to begin this route or 2 to go back\n")
        return choice

    def tracking_wrapper(self, in_tracker):
        """Begins the input/output for the Tracking mode.

        Attributes:
            in_tracker : Tracker
                The Tracker object for the user's selected Route.
        """
        class TrackerChangeObserverImpl(TrackerChangeObserver):
            """The concrete observer class for Tracker class updates in the UI.
            """
            def tracker_update(self, arg):
                """Simply clears the console and prints new Tracker info.
                """
                UI._clear_screen()
                UI._mini_tracking(arg)

        concrete_track_ob = TrackerChangeObserverImpl()
        # Add the newly created concrete observer to the Tracker ob set.
        in_tracker.add_tracker_change_ob(concrete_track_ob)

        self._display_tracking(in_tracker)

        # stops displaying tracking mode once finished the route
        # therefore this is where the observer should be removed
        in_tracker.rem_tracker_change_ob(concrete_track_ob)

    def _display_tracking(self, in_tracker):
        """The method that is the loop for the Tracking UI display.

        Parameters:
            in_tracker : Tracker
                The Tracker to display to the console.
        """
        choice = 'F'  # set choice to something invalid to enter the while loop
        # needs to determine if the user has reached the end point
        finished_route = in_tracker.has_finished()
        UI._clear_screen()

        # Continues whilst the user has not quit or completed the Route.
        while choice != '2' and not finished_route:
            self._mini_tracking(in_tracker)
            choice = input("")

            UI._clear_screen()
            if choice is '1':  # User has manually selected to complete a wp
                """Updates Tracker, which triggers its observer."""
                in_tracker.manually_complete_waypoint()
                UI._clear_screen()
                if in_tracker.has_finished():
                    print("\nPlease enter 2 to go back\n")
            elif choice is not '2':  # User has put random garbage into console.
                if in_tracker.has_finished():
                    UI._clear_screen()
                    print("\nPlease enter 2 to go back\n")
                else:
                    print("\nPlease enter 1 to manually complete waypoint"
                          " or 2 to go back\n")

    @staticmethod
    def _mini_tracking(in_tracker):
        """Static method to display Tracking information.

        If the user has finished and not exited, has a nice little extra thing.
        """
        print("---------------------------------------------\n"
              "- - - - - - - - Tracking Mode - - - - - - - -\n"
              "---------------------------------------------\n\n")
        if not in_tracker.has_finished():
            print("\t1. Manually complete this waypoint\n"
                  "\t2. Finish early\n\n")
            print("{}".format(in_tracker.__str__()))
        else:
            print("\t\t***You have finished!***")
            print("\t\t\tWay to Go!\n")
            print("\t2. Exit\n\n")
        print("\nYour selection:")
