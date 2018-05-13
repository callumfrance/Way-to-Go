import os


class UI:
    """The original view class"""

    @staticmethod
    def __clear_screen():
        """Clears the screen to allow new info to be printed"""
        os.system('cls' if os.name == 'nt' else 'clear')

    def display_main_menu(self, in_directory):
        """The starting menu from which all courses of action sprout from.
        """
        choice = 10
        while choice != 1 or choice != 2 or choice != 3:
        # while choice is not A or B or any valid route_list number
            self.__clear_screen()
            print("-----------------------------------------\n"
                  "- - - - - - - - Way-to-Go - - - - - - - -\n"
                  "-----------------------------------------\n\n")
            print("\tA. Update routes \n"
                  "\tB. Exit\n\n")
            print("{}".format(in_directory.__str__()))
            choice = int(input("\n> "))
        return choice

    def display_one_route(self, in_route):
        """Displays a Route and its segments.

        Used to determine if a user wants to 'go' on this route.
        """
        choice = 10
        while choice != 1 or choice != 2:
            self.__clear_screen()
            print("---------------------------------------------\n"
                "- - - - - - - - Route View  - - - - - - - - -\n"
                "---------------------------------------------\n\n")
            print("\t1. Begin route\n"
                "\t2. Back\n\n")
            print("{}".format(in_route.__str__()))
            choice = int(input("\n> "))
            if choice != 1 or choice != 2:
                print("\nPlease enter 1 to begin this route or 2 to go back\n")
        return choice

    def display_tracking(self, in_tracker):
        """The console output of the Tracking mode of the program.
        """
        self.__clear_screen()
        print("---------------------------------------------\n"
              "- - - - - - - - Tracking Mode - - - - - - - -\n"
              "---------------------------------------------\n\n")
        print("{}".format(in_tracker.__str__()))


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
