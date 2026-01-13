"""
Day 11: Sum of Digits

Question:
Find the sum of digits of a number.
"""

# Solution
n = 98765
total = 0
while n:
    total += n % 10
    n //= 10
print(total)
