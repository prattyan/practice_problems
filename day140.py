"""
Day 140: Compose Functions

Question:
Write a function that composes two functions.
"""

# Solution
def compose(f, g):
    return lambda x: f(g(x))

inc = lambda x: x + 1
double = lambda x: x * 2
print(compose(inc, double)(5))
