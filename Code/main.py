#!/usr/bin/python3
"""
Way-to-Go Main Class

Run this class in the console to launch the Way-to-Go program
"""

# Author: Callum France


from Controller import Controller

if __name__ == '__main__':
    """ Main program execution.
    
    Creates a controller class and begins the program with the main menu.
    """
    con = Controller()
    con.main_menu()
