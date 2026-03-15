"""
Day 57: Merge Two Sorted Lists

Question:
Merge two sorted lists into one sorted list.
"""

# Solution
def merge(a, b):
    i = j = 0
    out = []
    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            out.append(a[i]); i += 1
        else:
            out.append(b[j]); j += 1
    return out + a[i:] + b[j:]

print(merge([1, 3, 5, 7], [2, 4, 6, 8, 10]))
