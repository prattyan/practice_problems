"""
Day 107: GCD Using Recursion

Question:
Compute the GCD recursively.
"""

# Solution
def gcd(a, b):
    return a if b == 0 else gcd(b, a % b)

print(gcd(84, 36))
