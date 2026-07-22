"""
Day 114: Counting Sort

Question:
Sort non-negative integers using counting sort.
"""

# Solution
def counting_sort(a):
    cnt = [0] * (max(a) + 1)
    for x in a:
        cnt[x] += 1
    out = []
    for v, c in enumerate(cnt):
        out.extend([v] * c)
    return out

print(counting_sort([4, 2, 2, 8, 3, 3, 1]))
