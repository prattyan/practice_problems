"""
Day 141: Power of Two Check

Question:
Check if a number is a power of two using bit tricks.
"""

# Solution
def is_pow2(n):
    return n > 0 and n & (n - 1) == 0

print([n for n in (1, 2, 3, 16, 18, 64) if is_pow2(n)])
