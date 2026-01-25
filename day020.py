"""
Day 20: Armstrong Number

Question:
Check whether a number is an Armstrong number.
"""

# Solution
def is_armstrong(n):
    digits = str(n)
    return n == sum(int(d) ** len(digits) for d in digits)

print([n for n in (153, 370, 371, 123, 9474) if is_armstrong(n)])
