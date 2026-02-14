"""
Day 31: Number Triangle Pattern

Question:
Print a number triangle (1, 12, 123 ...).
"""

# Solution
n = 5
for i in range(1, n + 1):
    print("".join(str(j) for j in range(1, i + 1)))
