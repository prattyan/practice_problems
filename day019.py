"""
Day 19: LCM of Two Numbers

Question:
Find the LCM of two numbers.
"""

# Solution
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

a, b = 12, 18
print(a * b // gcd(a, b))
