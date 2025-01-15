#!/usr/bin/python3
print(", ".join("{:d}{:d}".format(i, j) for i in range(10) for j in range(i + 1, 10)))
