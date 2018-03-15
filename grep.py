#!/usr/bin/env python
"""Usage: grep.py PATTERN FILE

Search for lines in FILE containing PATTERN.
PATTERN can be regex.
"""
# = __doc__

import sys
try:
    import regex as re
except ModuleNotFoundError:
    print("regex module not found, using re", file=sys.stderr)
    import re

try:
    pattern, path = sys.argv[1:]
except ValueError:
    print(__doc__.strip(), file=sys.stderr)
    sys.exit(1)

try:
    with open(path) as file:
        for line in file:
            if re.search(pattern, line):
                print(line, end="")
except FileNotFoundError:
    print("file not found:", path, file=sys.stderr)
    sys.exit(1)