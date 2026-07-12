"""
Day 106: Palindrome Using Recursion

Question:
Check a palindrome recursively.
"""

# Solution
def is_pal(s):
    if len(s) < 2:
        return True
    return s[0] == s[-1] and is_pal(s[1:-1])

print(is_pal("racecar"), is_pal("hello"))
