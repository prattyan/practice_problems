"""
Day 21: Reverse a Number

Question:
Reverse the digits of an integer.
"""

# Solution
n = 12345
rev = 0
while n:
    rev = rev * 10 + n % 10
    n //= 10
print(rev)
