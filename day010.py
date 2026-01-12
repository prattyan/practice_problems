"""
Day 10: Count Vowels

Question:
Count the vowels in a string.
"""

# Solution
s = "Programming is fun"
print(sum(1 for ch in s.lower() if ch in "aeiou"))
