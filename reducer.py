#!/usr/bin/env python
import sys

# Initialize variables to store the current word and count
current_word = None
current_count = 0
word = None

# Input comes from standard input (STDIN)
for line in sys.stdin:
    line = line.strip()

    # Split the line into word and count
    try:
        word, count = line.split('\t', 1)  # Split by tab, not spaces
        count = int(count)  # Convert count to an integer
    except ValueError:
        # If count is not a number, skip the line
        continue

    # If the word is the same as the current word, increment the count
    if current_word == word:
        current_count += count
    else:
        # If the word has changed, print the current word and its count
        if current_word:
            print('%s\t%s' % (current_word, current_count))
        current_word = word
        current_count = count

# Print the last word's count if it exists
if current_word == word:
    print('%s\t%s' % (current_word, current_count))