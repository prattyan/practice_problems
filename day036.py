"""
Day 36: Decimal to Binary

Question:
Convert a decimal number to binary manually.
"""

# Solution
n = 45
bits = ""
while n:
    bits = str(n % 2) + bits
    n //= 2
print(bits or "0")
