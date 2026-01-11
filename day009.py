"""
Day 9: Palindrome String

Question:
Check if a string is a palindrome (ignore case and spaces).
"""

# Solution
s = "A man a plan a canal Panama"
t = "".join(s.lower().split())
print(t == t[::-1])
