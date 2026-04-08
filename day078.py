"""
Day 78: Row and Column Sums

Question:
Print the sum of every row and column of a matrix.
"""

# Solution
m = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print("Rows:", [sum(r) for r in m])
print("Cols:", [sum(c) for c in zip(*m)])
