"""
Day 43: Capitalize Each Word

Question:
Capitalize the first letter of each word.
"""

# Solution
s = "learning python is fun"
print(" ".join(w.capitalize() for w in s.split()))
