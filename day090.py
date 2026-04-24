"""
Day 90: Sort Tuples by Second Element

Question:
Sort a list of tuples by the second element.
"""

# Solution
a = [("a", 3), ("b", 1), ("c", 2)]
print(sorted(a, key=lambda t: t[1]))
