#!/usr/bin/env python

import sys

with open(sys.argv[2]) as file:
    for line in file:
        if sys.argv[1] in line:
            print(line, end="")