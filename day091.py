"""
Day 91: Common in Three Lists

Question:
Find elements common to three lists.
"""

# Solution
a, b, c = [1, 2, 3, 4], [2, 3, 4, 5], [3, 4, 5, 6]
print(sorted(set(a) & set(b) & set(c)))
