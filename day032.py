"""
Day 32: Primes in a Range

Question:
Print all prime numbers between 1 and 50.
"""

# Solution
def is_prime(n):
    return n > 1 and all(n % i for i in range(2, int(n ** 0.5) + 1))

print([n for n in range(1, 51) if is_prime(n)])
