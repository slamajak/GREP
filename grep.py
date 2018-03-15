#!/usr/bin/env python
"""Usage: grep.py PATTERN FILE...

Search for lines in FILE(S) containing PATTERN.
PATTERN can be regex.
"""
# = __doc__

import sys
try:
    import regex as re
except ModuleNotFoundError:
    print("regex module not found, using re", file=sys.stderr)
    import re


def parse_argv(argv):
    if len(argv) < 2:
        print(__doc__.strip(), file=sys.stderr)
        sys.exit(1)
    else:
        return argv[0], argv[1:]


def grep(file, pattern):
    for line in file:
        if re.search(pattern, line):
            print(line, end="")


def main(argv):
    pattern, paths = parse_argv(argv)
    for path in paths:
        try:
            with open(path) as file:
                grep(file, pattern)
        except FileNotFoundError:
            print("file not found:", path, file=sys.stderr)
            sys.exit(1)


if __name__ == "__main__":
    main(sys.argv[1:])
