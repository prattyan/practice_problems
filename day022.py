"""
Day 22: Sum of First N Natural Numbers

Question:
Find the sum of the first n natural numbers using a loop and a formula.
"""

# Solution
n = 100
print(sum(range(1, n + 1)), n * (n + 1) // 2)
