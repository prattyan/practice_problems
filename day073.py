"""
Day 73: Find Duplicate

Question:
Find a duplicate number in a list.
"""

# Solution
a = [3, 1, 3, 4, 2]
seen = set()
for x in a:
    if x in seen:
        print("Duplicate:", x)
        break
    seen.add(x)
