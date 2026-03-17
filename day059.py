"""
Day 59: Rotate List by K

Question:
Rotate a list to the right by k positions.
"""

# Solution
def rotate(a, k):
    k %= len(a)
    return a[-k:] + a[:-k]

print(rotate([1, 2, 3, 4, 5, 6, 7], 3))
