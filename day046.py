"""
Day 46: Is String Numeric

Question:
Check whether a string represents an integer or a float.
"""

# Solution
def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

print([is_number(x) for x in ("12", "3.14", "-7", "abc", "1e5", "")])
