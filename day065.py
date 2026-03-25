"""
Day 65: Element Frequency

Question:
Count the frequency of each element in a list.
"""

# Solution
from collections import Counter
a = ["a", "b", "a", "c", "b", "a"]
print(dict(Counter(a)))
