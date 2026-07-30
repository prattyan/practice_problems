"""
Day 119: Prime Factorization

Question:
Find the prime factors of a number.
"""

# Solution
def prime_factors(n):
    f, d = [], 2
    while d * d <= n:
        while n % d == 0:
            f.append(d)
            n //= d
        d += 1
    if n > 1:
        f.append(n)
    return f

print(prime_factors(360))
