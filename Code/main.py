#!/usr/bin/pyton3
import os

@staticmethod
def clear_screen():
    """Clears the screen before printing again."""
    os.system('cls' if os.name == 'nt' else 'clear')

@staticmethod
def main_menu():
    clear_screen()
    print( "Welcome to Way to Go \n\n \
            \t1. View current routes \n \
            \t2. Update routes \n \
            \t3. Exit")
    choiceNum = int(input("> "))
    if choiceNum == 1:
        # view current routes
    elif choiceNum == 2:
        # update routes
    elif choiceNum == 3:
        print("Exiting..")
        quit()
    else
        main_menu()
