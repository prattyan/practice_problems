"""
Day 5: Factorial

Question:
Compute the factorial of a number using a loop.
"""

# Solution
n = 6
f = 1
for i in range(2, n + 1):
    f *= i
print(f"{n}! =", f)
