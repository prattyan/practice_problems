"""
Day 34: FizzBuzz

Question:
Print 1..15; multiples of 3 -> Fizz, 5 -> Buzz, both -> FizzBuzz.
"""

# Solution
for i in range(1, 16):
    if i % 15 == 0: print("FizzBuzz")
    elif i % 3 == 0: print("Fizz")
    elif i % 5 == 0: print("Buzz")
    else: print(i)
