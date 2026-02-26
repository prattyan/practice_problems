"""
Day 42: First Non-Repeating Character

Question:
Find the first non-repeating character in a string.
"""

# Solution
from collections import Counter
s = "swiss"
cnt = Counter(s)
print(next((c for c in s if cnt[c] == 1), None))
