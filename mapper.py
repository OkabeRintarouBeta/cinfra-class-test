#!/usr/bin/env python
import sys

# Word Count Example
for line in sys.stdin:
    line = line.strip()  
    words = line.split()  

    for word in words:
        print(f"{word}\t1")

        
