"""
Day 64: Cumulative Sum

Question:
Compute the running (prefix) sum of a list.
"""

# Solution
from itertools import accumulate
a = [1, 2, 3, 4, 5]
print(list(accumulate(a)))
