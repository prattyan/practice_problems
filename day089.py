"""
Day 89: Tuple Unpacking

Question:
Unpack a tuple into variables and use extended unpacking.
"""

# Solution
t = (1, 2, 3, 4, 5)
first, *middle, last = t
print(first, middle, last)
