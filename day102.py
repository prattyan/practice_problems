"""
Day 102: Fibonacci with Memoization

Question:
Compute the nth Fibonacci number recursively with caching.
"""

# Solution
from functools import lru_cache

@lru_cache(maxsize=None)
def fib(n):
    return n if n < 2 else fib(n - 1) + fib(n - 2)

print(fib(50))
