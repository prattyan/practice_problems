"""
Day 122: Convert to Any Base

Question:
Convert a decimal number to any base from 2 to 16.
"""

# Solution
def to_base(n, base):
    digits = "0123456789ABCDEF"
    if n == 0:
        return "0"
    s = ""
    while n:
        s = digits[n % base] + s
        n //= base
    return s

print(to_base(255, 2), to_base(255, 8), to_base(255, 16))
