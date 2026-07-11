"""
Day 105: Reverse String Recursively

Question:
Reverse a string using recursion.
"""

# Solution
def rev(s):
    return s if len(s) <= 1 else rev(s[1:]) + s[0]

print(rev("recursion"))
