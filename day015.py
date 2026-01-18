"""
Day 15: Leap Year

Question:
Check whether a year is a leap year.
"""

# Solution
def is_leap(y):
    return y % 4 == 0 and (y % 100 != 0 or y % 400 == 0)

for y in (1900, 2000, 2024, 2023):
    print(y, is_leap(y))
