import sys
import os

sys.path.append('../')

from Model.TrackerModel.tracker_change_observer import TrackerChangeObserver
from Model.DirectoryModel.dir_update_observer import DirUpdateObserver


class UI:
    """The original view class"""

    @staticmethod
    def __clear_screen():
        """Clears the screen to allow new info to be printed"""
        os.system('cls' if os.name == 'nt' else 'clear')

    def main_menu_wrapper(self, in_directory):
        # create a new observer for Directory updates
        class DirUpdateObserverImpl(DirUpdateObserver):
            def dir_update(self, arg):
                """Calls the main menu again with the new Directory fields."""
                UI._display_main_menu(arg)

        concrete_dir_update_ob = DirUpdateObserverImpl()
        in_directory.add_dir_wide_update_ob(concrete_dir_update_ob)

        choice = self._display_main_menu(in_directory)

        in_directory.rem_dir_wide_update_ob(concrete_dir_update_ob)
        return choice

    @staticmethod
    def _display_main_menu(in_directory):
        valid_route_select = False
        choice = 'F'
        pattern = ['a', 'A', 'b', 'B']
        UI.__clear_screen()

        # while choice is not A or B or any valid route_list number
        while choice not in pattern and not valid_route_select:
            print("-----------------------------------------\n"
                  "- - - - - - - - Way-to-Go - - - - - - - -\n"
                  "-----------------------------------------\n\n")
            print("\tA. Update routes \n"
                  "\tB. Exit\n\n")
            print("{}".format(in_directory.__str__()))
            choice = input("\n> ")
            UI.__clear_screen()

            if choice.isdigit() and int(choice) > 0:
                """Check if user has entered an appropriate number or not"""
                choice = int(choice)
                if 1 <= choice < len(in_directory.route_dict):
                    valid_route_select = True
            if not valid_route_select:
                print("Please select a valid route number, update, or exit.\n")
        return choice

    def display_one_route(self, in_route):
        """Displays a Route and its segments.

        Used to determine if a user wants to 'go' on this route.
        """

        choice = 'F'
        self.__clear_screen()
        while choice != 1 and choice != 2:
            self.__clear_screen()
            print("---------------------------------------------\n"
                  "- - - - - - - - Route View  - - - - - - - - -\n"
                  "---------------------------------------------\n\n")
            print("\t1. Begin route\n"
                  "\t2. Back\n\n")
            print("{}".format(in_route.__str__()))
            choice = int(input("\n> "))
            self.__clear_screen()
            if choice != 1 or choice != 2:
                print("\nPlease enter 1 to begin this route or 2 to go back\n")
        return choice

    def tracking_wrapper(self, in_tracker):
        class TrackerChangeObserverImpl(TrackerChangeObserver):
            def tracker_update(self, arg):
                UI._display_tracking(arg)

        concrete_track_ob = TrackerChangeObserverImpl()
        in_tracker.add_track_ob(concrete_track_ob)

        self._display_tracking(in_tracker)

        # stops displaying tracking mode once finished the route
        # therefore this is where the observer should be removed
        in_tracker.rem_curr_loc_ob(concrete_track_ob)

    @staticmethod
    def _display_tracking(in_tracker):
        choice = 'F'
        UI.__clear_screen()
        # needs to determine if the user has reached the end point
        finished_route = in_tracker.has_finished()

        while choice != 2 or not finished_route:
            print("---------------------------------------------\n"
                  "- - - - - - - - Tracking Mode - - - - - - - -\n"
                  "---------------------------------------------\n\n")
            print("\t1. Manually complete this waypoint\n"
                  "\t2. Finish early\n\n")
            print("{}".format(in_tracker.__str__()))
            choice = int(input("\n> "))
            UI.__clear_screen()

            if choice is 1:
                """Updates Tracker, which triggers its observer."""
                in_tracker.manually_complete_waypoint()
            elif choice is not 2:
                print("\nPlease enter 1 to manually complete waypoint"
                      "or 2 to go back\n")
            # condition to show that a route has been finished goes here

# print("\tCurrent Location: {}".format(in_tracker.curr_loc))
# print("\tNext Waypoint: {}".format(in_tracker.next_waypoint))
# print("\tRemaining distance: {} m".format(in_tracker.remaining[0]))
# print("\tRemaining climb: {} m".format(in_tracker.remaining[1]))
# print("\tRemaining descent: {} m".format(in_tracker.remaining[2]))


# --------------------
# Put code here to print out all Directory route info
#   route name
#   route description
#   start and end coordinates
#   total distance (horizontal, climb, descent)
# --------------------
