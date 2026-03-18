"""
Day 60: Common Elements

Question:
Find common elements between two lists.
"""

# Solution
a = [1, 2, 3, 4, 5]
b = [4, 5, 6, 7]
print(sorted(set(a) & set(b)))
