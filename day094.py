"""
Day 94: Product of Array Except Self

Question:
For each index, find the product of all other elements (no division).
"""

# Solution
def product_except_self(a):
    n = len(a)
    res = [1] * n
    left = 1
    for i in range(n):
        res[i] = left
        left *= a[i]
    right = 1
    for i in range(n - 1, -1, -1):
        res[i] *= right
        right *= a[i]
    return res

print(product_except_self([1, 2, 3, 4]))
