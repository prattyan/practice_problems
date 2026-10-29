"""
Day 176: Age Calculator

Question:
Calculate age in years from a birth date.
"""

# Solution
from datetime import date

def age(born, today):
    return today.year - born.year - ((today.month, today.day) < (born.month, born.day))

print(age(date(2000, 8, 25), date(2026, 11, 13)))
