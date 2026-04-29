"""
Day 95: Split List into Chunks

Question:
Split a list into chunks of size k.
"""

# Solution
a = list(range(1, 11))
k = 3
print([a[i:i + k] for i in range(0, len(a), k)])
