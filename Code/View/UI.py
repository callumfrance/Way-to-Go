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
    def __clear_screen():
        """Clears the console to allow new info to be printed"""
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
        choice = 5
        # Must check if user input matches any route name listed in the Dir
        pattern = list(in_directory.route_dict.keys())
        UI.__clear_screen()

        # while choice is not A or B or any valid route_list number
        while choice not in pattern and choice is not 1 and choice is not 2:
            print("-----------------------------------------\n"
                  "- - - - - - - - Way-to-Go - - - - - - - -\n"
                  "-----------------------------------------\n\n")
            print("\t1. Update routes \n"
                  "\t2. Exit\n\n")
            print("{}".format(in_directory.__str__()))
            choice = input("\n> ")
            UI.__clear_screen()

            if choice not in pattern:
                try:
                    choice = int(choice)
                except ValueError:
                    pass
                if choice is not 1 and choice is not 2:
                    print("Please select a valid route name, update, or exit.\n")

        return choice

    def display_one_route(self, in_route):
        """Displays a Route and its segments.

        Used to determine if a user wants to 'go' on this route.
        """

        choice = 'F'
        self.__clear_screen()
        while choice != 1 and choice != 2:
            print("---------------------------------------------\n"
                  "- - - - - - - - Route View  - - - - - - - - -\n"
                  "---------------------------------------------\n\n")
            print("\t1. Begin route\n"
                  "\t2. Back\n\n")
            print("{}".format(in_route.__str__()))
            try:
                choice = int(input("\n> "))
            except ValueError:
                pass
            self.__clear_screen()
            if choice != 1 or choice != 2:
                print("\nPlease enter 1 to begin this route or 2 to go back\n")
        return choice

    def tracking_wrapper(self, in_tracker):
        class TrackerChangeObserverImpl(TrackerChangeObserver):
            def tracker_update(self, arg):
                UI._display_tracking(arg)

        concrete_track_ob = TrackerChangeObserverImpl()
        in_tracker.add_tracker_change_ob(concrete_track_ob)

        self._display_tracking(in_tracker)

        # stops displaying tracking mode once finished the route
        # therefore this is where the observer should be removed
        in_tracker.rem_tracker_change_ob(concrete_track_ob)

    @staticmethod
    def _display_tracking(in_tracker):
        choice = 'F'
        # needs to determine if the user has reached the end point
        finished_route = in_tracker.has_finished()
        UI.__clear_screen()

        while choice != 2 and not finished_route:
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
