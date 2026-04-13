"""
Day 81: Sort Dictionary by Value

Question:
Sort a dictionary by its values.
"""

# Solution
d = {"apple": 5, "banana": 2, "cherry": 9}
print(dict(sorted(d.items(), key=lambda kv: kv[1])))
