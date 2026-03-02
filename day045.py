"""
Day 45: Replace Vowels

Question:
Replace all vowels in a string with '*'.
"""

# Solution
s = "programming language"
print("".join("*" if c.lower() in "aeiou" else c for c in s))
