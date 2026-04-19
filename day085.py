"""
Day 85: Dictionary from Two Lists

Question:
Create a dictionary from a list of keys and a list of values.
"""

# Solution
keys = ["name", "age", "city"]
vals = ["Ravi", 25, "Kolkata"]
print(dict(zip(keys, vals)))
