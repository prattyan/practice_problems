"""
Day 28: Simple Calculator

Question:
Build a simple calculator supporting + - * /.
"""

# Solution
def calc(a, op, b):
    if op == "+": return a + b
    if op == "-": return a - b
    if op == "*": return a * b
    if op == "/": return a / b if b != 0 else "Cannot divide by zero"
    return "Invalid operator"

print(calc(8, "+", 2), calc(8, "-", 2), calc(8, "*", 2), calc(8, "/", 0))
