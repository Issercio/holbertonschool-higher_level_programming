#!/usr/bin/python3
'''read a file
'''


def read_file(filename=""):
    """Read a text file (UTF-8) and print its content to stdout."""
    with open(filename, "r", encoding="utf-8") as file:
        print(file.read(), end="")
