#! /usr/bin/env python
# This makes an egrep.py command
#
# because input is stdin and output is stdout, you can use this is in a pipe command
# E.G.
# cat README.md | ch9/egrep.py Data 
import sys, regex as re
#
# sys.argv is the list of command-line arguments
# sys.argv[0] is the name of the program itself
# sys.argv[1] will be the regext specified at the command line
regex = sys.argv[1]

for line in sys.stdin:
    # if it matches the regex, return the line to stdout
    if re.search(regex,line):
        sys.stdout.write(line)