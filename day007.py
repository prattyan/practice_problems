"""
Day 7: Prime Check

Question:
Check whether a number is prime.
"""

# Solution
def is_prime(n):
    if n < 2:
        return False
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True

for n in (1, 2, 17, 18, 97):
    print(n, is_prime(n))
