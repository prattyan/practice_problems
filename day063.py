"""
Day 63: Two Sum

Question:
Return indices of two numbers that add up to a target.
"""

# Solution
def two_sum(nums, target):
    seen = {}
    for i, n in enumerate(nums):
        if target - n in seen:
            return seen[target - n], i
        seen[n] = i

print(two_sum([2, 7, 11, 15], 9))
