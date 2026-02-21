"""
Day 38: Count Upper and Lower Case

Question:
Count uppercase and lowercase letters in a string.
"""

# Solution
s = "Hello World From Python"
print("Upper:", sum(c.isupper() for c in s))
print("Lower:", sum(c.islower() for c in s))
