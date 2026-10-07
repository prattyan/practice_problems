"""
Day 154: Stack Class

Question:
Implement a Stack class with push, pop, peek and is_empty.
"""

# Solution
class Stack:
    def __init__(self):
        self.items = []

    def push(self, x): self.items.append(x)
    def pop(self): return self.items.pop() if self.items else None
    def peek(self): return self.items[-1] if self.items else None
    def is_empty(self): return not self.items

s = Stack()
s.push(1); s.push(2); s.push(3)
print(s.pop(), s.peek(), s.is_empty())
