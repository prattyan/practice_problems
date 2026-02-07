"""
Day 26: Positive, Negative or Zero

Question:
Check whether a number is positive, negative or zero.
"""

# Solution
for n in (5, -3, 0):
    if n > 0:
        print(n, "positive")
    elif n < 0:
        print(n, "negative")
    else:
        print(n, "zero")
