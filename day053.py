"""
Day 53: Second Largest Element

Question:
Find the second largest element in a list.
"""

# Solution
nums = [10, 45, 3, 99, 45, 72]
unique = sorted(set(nums))
print(unique[-2])
