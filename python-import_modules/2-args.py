#!/usr/bin/python3
import sys

if __name__ == "__main__":
    num_args = len(sys.argv) - 1  # exclude the script name
    if num_args == 0:
        print("0 arguments.")
    else:
        print(f"{num_args} argument{'' if num_args == 1 else 's'}:")
        for i in range(1, num_args + 1):
            print(f"{i}: {sys.argv[i]}")
