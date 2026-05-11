"""
Day 99: Leaders in an Array

Question:
Find elements greater than everything to their right.
"""

# Solution
a = [16, 17, 4, 3, 5, 2]
leaders = []
mx = float("-inf")
for x in reversed(a):
    if x > mx:
        leaders.append(x)
        mx = x
print(leaders[::-1])
