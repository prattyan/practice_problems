"""
Day 75: Matrix Addition

Question:
Add two matrices.
"""

# Solution
a = [[1, 2], [3, 4]]
b = [[5, 6], [7, 8]]
print([[a[i][j] + b[i][j] for j in range(2)] for i in range(2)])
