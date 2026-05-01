"""
Day 97: Group Anagrams

Question:
Group words that are anagrams of each other.
"""

# Solution
from collections import defaultdict
words = ["eat", "tea", "tan", "ate", "nat", "bat"]
g = defaultdict(list)
for w in words:
    g["".join(sorted(w))].append(w)
print(list(g.values()))
