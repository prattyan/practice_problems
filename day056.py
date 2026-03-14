"""
Day 56: Bubble Sort

Question:
Sort a list using bubble sort.
"""

# Solution
def bubble_sort(a):
    a = a[:]
    n = len(a)
    for i in range(n):
        swapped = False
        for j in range(n - i - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                swapped = True
        if not swapped:
            break
    return a

print(bubble_sort([64, 34, 25, 12, 22, 11, 90]))
