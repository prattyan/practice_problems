"""
Day 70: Linear Search

Question:
Find the index of an element using linear search.
"""

# Solution
def linear_search(a, target):
    for i, x in enumerate(a):
        if x == target:
            return i
    return -1

print(linear_search([5, 3, 8, 1], 8), linear_search([5, 3, 8, 1], 10))
