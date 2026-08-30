"""
Day 135: Lambda, map and filter

Question:
Use lambda with map and filter on a list.
"""

# Solution
nums = [1, 2, 3, 4, 5, 6]
print(list(map(lambda x: x ** 2, nums)))
print(list(filter(lambda x: x % 2 == 0, nums)))
