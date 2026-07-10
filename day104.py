"""
Day 104: Power Using Recursion

Question:
Compute x^n using fast exponentiation (recursion).
"""

# Solution
def power(x, n):
    if n == 0:
        return 1
    half = power(x, n // 2)
    return half * half if n % 2 == 0 else half * half * x

print(power(2, 10), power(3, 7))
