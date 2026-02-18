"""
Day 35: Binary to Decimal

Question:
Convert a binary number (as string) to decimal manually.
"""

# Solution
b = "101101"
dec = 0
for bit in b:
    dec = dec * 2 + int(bit)
print(dec)
