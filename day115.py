"""
Day 115: Permutations of a String

Question:
Generate all permutations of a string recursively.
"""

# Solution
def perms(s):
    if len(s) <= 1:
        return [s]
    out = []
    for i, ch in enumerate(s):
        for p in perms(s[:i] + s[i + 1:]):
            out.append(ch + p)
    return out

print(perms("abc"))
