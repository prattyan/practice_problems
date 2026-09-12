"""
Day 142: Count Set Bits

Question:
Count the number of 1 bits in an integer.
"""

# Solution
def count_bits(n):
    c = 0
    while n:
        n &= n - 1
        c += 1
    return c

print(count_bits(29), bin(29))
