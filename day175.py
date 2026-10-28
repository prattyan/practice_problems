"""
Day 175: Days Between Two Dates

Question:
Calculate the number of days between two dates.
"""

# Solution
from datetime import date

d1, d2 = date(2024, 1, 15), date(2026, 11, 13)
print((d2 - d1).days, "days")
