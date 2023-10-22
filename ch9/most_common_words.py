#! /usr/bin/env python
import sys
from collections import Counter

#
# gets stdin and returns the most common words passed to the input
# the number of words returned is a parameter

try:
    num_words = int(sys.argv[1])
except:
    print("usage: most_common_words.py <num_words>")
    sys.exit()
#
# count the words
# the last if skips empty words?
counter = Counter(word.lower() for line in sys.stdin for word in line.strip().split() if word)

for word,count in counter.most_common(num_words):
    sys.stdout.write(f"{count:4} {word}\n")