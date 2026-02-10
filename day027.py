"""
Day 27: Grade Calculator

Question:
Assign a grade (A-F) based on marks.
"""

# Solution
def grade(m):
    if m >= 90: return "A"
    if m >= 80: return "B"
    if m >= 70: return "C"
    if m >= 60: return "D"
    return "F"

for m in (95, 83, 71, 65, 40):
    print(m, grade(m))
