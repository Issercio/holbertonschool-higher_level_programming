#!/usr/bin/python3
def uppercase(str):
    print("".join("{:c}".format(ord(c) - 32) if 97 <= ord(c) <= 122 else c for c in str))
