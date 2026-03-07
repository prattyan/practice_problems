"""
Day 49: Count Substring Occurrences

Question:
Count how many times a substring occurs (including overlaps).
"""

# Solution
s, sub = "aaaa", "aa"
count = sum(1 for i in range(len(s) - len(sub) + 1) if s[i:i + len(sub)] == sub)
print(count)
