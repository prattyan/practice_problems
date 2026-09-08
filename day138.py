"""
Day 138: Variable Arguments

Question:
Write a function using *args and **kwargs.
"""

# Solution
def info(*args, **kwargs):
    print("Args:", args)
    print("Kwargs:", kwargs)
    return sum(args)

print(info(1, 2, 3, name="Raj", city="Delhi"))
