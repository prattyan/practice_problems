"""
Day 25: Perfect Number

Question:
Check whether a number is perfect (sum of proper divisors equals the number).
"""

# Solution
def is_perfect(n):
    return n > 1 and sum(i for i in range(1, n) if n % i == 0) == n

print([n for n in range(1, 500) if is_perfect(n)])
