"""
Day 93: Maximum Subarray Sum (Kadane)

Question:
Find the contiguous subarray with the largest sum.
"""

# Solution
def kadane(a):
    best = cur = a[0]
    for x in a[1:]:
        cur = max(x, cur + x)
        best = max(best, cur)
    return best

print(kadane([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
