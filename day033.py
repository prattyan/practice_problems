"""
Day 33: Sum of Even Numbers

Question:
Find the sum of all even numbers from 1 to n.
"""

# Solution
n = 20
print(sum(i for i in range(1, n + 1) if i % 2 == 0))
