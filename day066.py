"""
Day 66: Most Frequent Element

Question:
Find the most frequent element in a list.
"""

# Solution
from collections import Counter
a = [1, 3, 2, 3, 3, 1, 2, 3]
print(Counter(a).most_common(1)[0])
