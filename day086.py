"""
Day 86: Key with Max Value

Question:
Find the key that has the maximum value in a dictionary.
"""

# Solution
d = {"a": 10, "b": 45, "c": 22}
print(max(d, key=d.get))
