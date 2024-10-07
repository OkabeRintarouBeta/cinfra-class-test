#!/usr/bin/env python
import sys

# Word Count Example
for line in sys.stdin:
    line = line.strip()  # Remove leading and trailing whitespaces
    words = line.split()  # Split the line into words

    for word in words:
        # Write the result to standard output (STDOUT)
        print('%s\t%s' % (word, 1))  # Emit the word followed by a count of 1
