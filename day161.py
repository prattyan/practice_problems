"""
Day 161: Graph BFS

Question:
Traverse a graph using breadth-first search.
"""

# Solution
from collections import deque

graph = {"A": ["B", "C"], "B": ["D", "E"], "C": ["F"], "D": [], "E": ["F"], "F": []}

def bfs(start):
    seen, order, q = {start}, [], deque([start])
    while q:
        node = q.popleft()
        order.append(node)
        for nb in graph[node]:
            if nb not in seen:
                seen.add(nb)
                q.append(nb)
    return order

print(bfs("A"))
