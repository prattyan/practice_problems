"""
Day 47: Remove Duplicate Characters

Question:
Remove duplicate characters from a string, keeping order.
"""

# Solution
s = "programming"
print("".join(dict.fromkeys(s)))
