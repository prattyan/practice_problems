"""
Day 110: Selection Sort

Question:
Sort a list using selection sort.
"""

# Solution
def selection_sort(a):
    a = a[:]
    for i in range(len(a)):
        m = min(range(i, len(a)), key=a.__getitem__)
        a[i], a[m] = a[m], a[i]
    return a

print(selection_sort([29, 10, 14, 37, 13]))
