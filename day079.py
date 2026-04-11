"""
Day 79: Pascal's Triangle

Question:
Print the first n rows of Pascal's triangle.
"""

# Solution
n = 6
row = [1]
for _ in range(n):
    print(" ".join(map(str, row)).center(30))
    row = [1] + [row[i] + row[i + 1] for i in range(len(row) - 1)] + [1]
