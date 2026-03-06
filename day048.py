"""
Day 48: Longest Word

Question:
Find the longest word in a sentence.
"""

# Solution
s = "The quick brown fox jumped over the lazy dog"
print(max(s.split(), key=len))
