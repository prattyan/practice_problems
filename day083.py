"""
Day 83: Group Words by Length

Question:
Group words by their length.
"""

# Solution
from collections import defaultdict
words = ["hi", "cat", "dog", "hello", "to", "world"]
groups = defaultdict(list)
for w in words:
    groups[len(w)].append(w)
print(dict(groups))
