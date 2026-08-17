"""
Day 128: Next Greater Element

Question:
For each element find the next greater element to its right (-1 if none).
"""

# Solution
def next_greater(a):
    res = [-1] * len(a)
    stack = []
    for i, x in enumerate(a):
        while stack and a[stack[-1]] < x:
            res[stack.pop()] = x
        stack.append(i)
    return res

print(next_greater([4, 5, 2, 25]))
