#!/usr/bin/python3


import sys

from os import path
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

filename = "add_item.json"

if path.exists(filename):
    my_item = load_from_json_file(filename)
else:
    my_item = []

my_item.extend(sys.argv[1:])

save_to_json_file(my_item, filename)
