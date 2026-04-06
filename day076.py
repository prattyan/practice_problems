"""
Day 76: Matrix Multiplication

Question:
Multiply two matrices.
"""

# Solution
a = [[1, 2], [3, 4]]
b = [[5, 6], [7, 8]]
res = [[sum(a[i][k] * b[k][j] for k in range(2)) for j in range(2)] for i in range(2)]
print(res)
