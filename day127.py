"""
Day 127: Queue Using deque

Question:
Implement a queue using collections.deque.
"""

# Solution
from collections import deque
q = deque()
q.append("a")
q.append("b")
q.append("c")
print(q.popleft(), list(q))
