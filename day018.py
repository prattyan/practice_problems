"""
Day 18: GCD of Two Numbers

Question:
Find the GCD of two numbers using Euclid's algorithm.
"""

# Solution
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

print(gcd(48, 18))
