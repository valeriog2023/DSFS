#! /usr/bin/env python
#
# because input is stdin and output is stdout, you can use this is in a pipe command
# E.G.
# cat README.md | ch9/egrep.py  .* | ch9/line_count.py 
import sys

count = 0

for lin in sys.stdin:
     count += 1

print(count)     