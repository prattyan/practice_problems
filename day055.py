"""
Day 55: Remove Duplicates Keeping Order

Question:
Remove duplicates from a list while preserving order.
"""

# Solution
a = [3, 1, 3, 2, 1, 5, 2]
print(list(dict.fromkeys(a)))
