"""
Day 77: Diagonal Sum

Question:
Find the sum of the main and secondary diagonals of a square matrix.
"""

# Solution
m = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
n = len(m)
print("Main:", sum(m[i][i] for i in range(n)))
print("Secondary:", sum(m[i][n - 1 - i] for i in range(n)))
