"""
Day 155: Queue Class

Question:
Implement a Queue class with enqueue, dequeue and size.
"""

# Solution
from collections import deque

class Queue:
    def __init__(self):
        self.q = deque()

    def enqueue(self, x): self.q.append(x)
    def dequeue(self): return self.q.popleft() if self.q else None
    def size(self): return len(self.q)

q = Queue()
for x in "abc":
    q.enqueue(x)
print(q.dequeue(), q.size())
