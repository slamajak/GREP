#!/usr/bin/env python

import sys
import regex as re

pattern, path = sys.argv[1:]
with open(path) as file:
    for line in file:
        if re.search(pattern, line):
            print(line, end="")