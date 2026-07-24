"""
Day 116: Generate All Subsets

Question:
Generate all subsets of a list.
"""

# Solution
def subsets(a):
    res = [[]]
    for x in a:
        res += [s + [x] for s in res]
    return res

print(subsets([1, 2, 3]))
