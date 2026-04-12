"""
Day 80: Merge Two Dictionaries

Question:
Merge two dictionaries (second overrides the first).
"""

# Solution
a = {"x": 1, "y": 2}
b = {"y": 3, "z": 4}
print({**a, **b})
