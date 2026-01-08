"""
Day 6: Fibonacci Series

Question:
Print the first n Fibonacci numbers.
"""

# Solution
n = 10
a, b = 0, 1
out = []
for _ in range(n):
    out.append(a)
    a, b = b, a + b
print(out)
