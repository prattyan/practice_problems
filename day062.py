"""
Day 62: Move Zeros to End

Question:
Move all zeros to the end while keeping the order of other elements.
"""

# Solution
a = [0, 1, 0, 3, 12]
print([x for x in a if x != 0] + [0] * a.count(0))
