"""
Day 82: Invert a Dictionary

Question:
Swap keys and values of a dictionary.
"""

# Solution
d = {"a": 1, "b": 2, "c": 3}
print({v: k for k, v in d.items()})
