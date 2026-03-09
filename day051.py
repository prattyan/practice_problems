"""
Day 51: Sum of a List

Question:
Find the sum of all elements in a list without using sum().
"""

# Solution
nums = [4, 8, 15, 16, 23, 42]
total = 0
for x in nums:
    total += x
print(total)
