#!/usr/bin/env python
import sys

# Word Count Example
for line in sys.stdin:
    line = line.strip()  # Remove leading and trailing whitespaces
    words = line.split()  # Split the line into words

    for word in words:
        print(f"{word}\t1")
