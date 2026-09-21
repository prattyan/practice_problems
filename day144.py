"""
Day 144: Climbing Stairs (DP)

Question:
Count ways to climb n stairs taking 1 or 2 steps at a time.
"""

# Solution
def ways(n):
    a, b = 1, 1
    for _ in range(n - 1):
        a, b = b, a + b
    return b

print(ways(5), ways(10))
