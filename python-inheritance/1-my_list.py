#!/usr/bin/python3
'''1-my_list.py
'''


class MyList(list):
    """A subclass of list that includes a method to print"""

    def print_sorted(self):
        """Prints the list"""
        print(sorted(self))
