"""
Day 101: Factorial Using Recursion

Question:
Compute factorial recursively.
"""

# Solution
def fact(n):
    return 1 if n <= 1 else n * fact(n - 1)

print(fact(7))
