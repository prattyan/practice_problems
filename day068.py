"""
Day 68: Remove All Occurrences

Question:
Remove all occurrences of a value from a list.
"""

# Solution
a = [1, 2, 3, 2, 4, 2]
print([x for x in a if x != 2])
