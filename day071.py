"""
Day 71: Binary Search

Question:
Implement iterative binary search on a sorted list.
"""

# Solution
def binary_search(a, target):
    lo, hi = 0, len(a) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if a[mid] == target: return mid
        if a[mid] < target: lo = mid + 1
        else: hi = mid - 1
    return -1

a = [1, 3, 5, 7, 9, 11]
print(binary_search(a, 7), binary_search(a, 4))
