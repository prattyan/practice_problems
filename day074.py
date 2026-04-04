"""
Day 74: Transpose Matrix

Question:
Transpose a matrix.
"""

# Solution
m = [[1, 2, 3], [4, 5, 6]]
print([list(r) for r in zip(*m)])
