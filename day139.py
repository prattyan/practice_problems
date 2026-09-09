"""
Day 139: Closure Counter

Question:
Create a counter using a closure.
"""

# Solution
def make_counter():
    count = 0
    def inc():
        nonlocal count
        count += 1
        return count
    return inc

c = make_counter()
print(c(), c(), c())
