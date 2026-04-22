"""
Day 88: Unique Elements in Two Lists

Question:
Find elements that appear in only one of the two lists.
"""

# Solution
a = [1, 2, 3, 4]
b = [3, 4, 5, 6]
print(sorted(set(a) ^ set(b)))
