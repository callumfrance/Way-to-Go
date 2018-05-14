import os
from dir_update_observer import DirUpdateObserver
from dir_route_retrieve_observer import DirRouteRetrieveObserver


class UI:
    """The original view class"""

    @staticmethod
    def __clear_screen():
        """Clears the screen to allow new info to be printed"""
        os.system('cls' if os.name == 'nt' else 'clear')

    def display_main_menu(self, in_directory):
        """The starting menu from which all courses of action sprout from.
        """

        # create a new observer for Directory updates
        concrete_dir_update_ob = DirUpdateObserverImpl()
        in_directory.add_dir_wide_update_ob(concrete_dir_update_ob)

        choice = 'F'
        pattern = ['a', 'A', 'b', 'B']
        # while choice is not A or B or any valid route_list number
        while choice not in pattern
                or not 1 <= choice <= len(in_directory.route_dict):
            self.__clear_screen()
            print("-----------------------------------------\n"
                  "- - - - - - - - Way-to-Go - - - - - - - -\n"
                  "-----------------------------------------\n\n")
            print("\tA. Update routes \n"
                  "\tB. Exit\n\n")
            print("{}".format(in_directory.__str__()))
            try:
                """Check if user has entered a number or not"""
                choice = int(input("\n> "))
            except ValueError e:
                choice = input("\n> ")

        in_directory.rem_dir_wide_update_ob(concrete_dir_update_ob)

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

    def display_tracking(self, in_tracker):
        """The console output of the Tracking mode of the program.
        """
        choice = 'F'
        finished_route = False
        self.__clear_screen()
        while choice != 1 and choice != 2 or not finished_route:
            print("---------------------------------------------\n"
                "- - - - - - - - Tracking Mode - - - - - - - -\n"
                "---------------------------------------------\n\n")
            print("\t1. Manually complete this waypoint\n"
                "\t2. Finish early\n\n")
            print("{}".format(in_tracker.__str__()))
            choice = int(input("\n> "))
            self.__clear_screen()
            if choice != 1 or choice != 2:
                print("\nPlease enter 1 to manually complete waypoint"
                      "or 2 to go back\n")
            # condition to show that a route has been finished goes here


    class DirUpdateObserverImpl(DirUpdateObserver):
        """Nested concrete observer class for Directory updates."""

        def dir_update(self, arg):
            """Calls the main menu again with the new Directory fields."""
            self.display_main_menu(arg)



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
