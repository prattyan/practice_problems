"""
Day 103: Sum of Digits Recursively

Question:
Find the sum of digits using recursion.
"""

# Solution
def digit_sum(n):
    return 0 if n == 0 else n % 10 + digit_sum(n // 10)

print(digit_sum(12345))
