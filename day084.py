"""
Day 84: Word Frequency

Question:
Count the frequency of words in a sentence.
"""

# Solution
from collections import Counter
s = "the cat and the hat and the bat"
print(Counter(s.split()))
