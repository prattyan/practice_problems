"""
Day 92: Count Pairs with Given Sum

Question:
Count pairs in a list whose sum equals a target.
"""

# Solution
from collections import Counter
a = [1, 5, 7, -1, 5]
target = 6
seen = Counter()
count = 0
for x in a:
    count += seen[target - x]
    seen[x] += 1
print(count)
