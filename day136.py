"""
Day 136: Simple Decorator

Question:
Write a decorator that logs function calls.
"""

# Solution
def logger(fn):
    def wrapper(*args, **kwargs):
        print(f"Calling {fn.__name__}{args}")
        result = fn(*args, **kwargs)
        print("Returned", result)
        return result
    return wrapper

@logger
def add(a, b):
    return a + b

add(3, 4)
