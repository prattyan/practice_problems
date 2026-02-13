"""
Day 30: Pyramid Pattern

Question:
Print a centered star pyramid.
"""

# Solution
n = 5
for i in range(1, n + 1):
    print(" " * (n - i) + "*" * (2 * i - 1))
