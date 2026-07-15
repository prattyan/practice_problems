"""
Day 109: Recursive Binary Search

Question:
Implement binary search recursively.
"""

# Solution
def bs(a, t, lo=0, hi=None):
    if hi is None:
        hi = len(a) - 1
    if lo > hi:
        return -1
    mid = (lo + hi) // 2
    if a[mid] == t: return mid
    if a[mid] < t: return bs(a, t, mid + 1, hi)
    return bs(a, t, lo, mid - 1)

print(bs([2, 4, 6, 8, 10, 12], 10))
