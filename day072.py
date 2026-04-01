"""
Day 72: Missing Number

Question:
Find the missing number in a list containing 1..n with one missing.
"""

# Solution
a = [1, 2, 4, 5, 6]
n = len(a) + 1
print(n * (n + 1) // 2 - sum(a))
