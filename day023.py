"""
Day 23: Power Without ** Operator

Question:
Compute base raised to exponent using a loop.
"""

# Solution
base, exp = 3, 5
result = 1
for _ in range(exp):
    result *= base
print(result)
