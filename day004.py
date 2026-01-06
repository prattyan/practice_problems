"""
Day 4: Largest of Three

Question:
Find the largest of three numbers without using max().
"""

# Solution
a, b, c = 14, 92, 37
largest = a
if b > largest: largest = b
if c > largest: largest = c
print("Largest:", largest)
