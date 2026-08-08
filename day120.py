"""
Day 120: Nth Fibonacci Iteratively

Question:
Compute the nth Fibonacci number in O(n) time and O(1) space.
"""

# Solution
def fib(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

print(fib(30))
