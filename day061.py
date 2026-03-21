"""
Day 61: Flatten Nested List

Question:
Flatten an arbitrarily nested list.
"""

# Solution
def flatten(lst):
    out = []
    for x in lst:
        if isinstance(x, list):
            out.extend(flatten(x))
        else:
            out.append(x)
    return out

print(flatten([1, [2, [3, 4]], [[5], 6]]))
