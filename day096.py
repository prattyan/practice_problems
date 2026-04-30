"""
Day 96: Zip and Unzip

Question:
Combine two lists with zip and then unzip them.
"""

# Solution
names = ["A", "B", "C"]
scores = [90, 80, 70]
pairs = list(zip(names, scores))
print(pairs)
n, s = zip(*pairs)
print(n, s)
