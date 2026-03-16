"""
Day 58: Count Even and Odd

Question:
Count even and odd numbers in a list.
"""

# Solution
nums = [1, 2, 3, 4, 5, 6, 7]
even = sum(1 for n in nums if n % 2 == 0)
print("Even:", even, "Odd:", len(nums) - even)
