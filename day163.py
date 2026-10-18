"""
Day 163: Shortest Path in Unweighted Graph

Question:
Find the shortest path between two nodes using BFS.
"""

# Solution
from collections import deque

graph = {"A": ["B", "C"], "B": ["D"], "C": ["D", "E"], "D": ["F"], "E": ["F"], "F": []}

def shortest(s, t):
    q, seen = deque([[s]]), {s}
    while q:
        path = q.popleft()
        if path[-1] == t:
            return path
        for nb in graph[path[-1]]:
            if nb not in seen:
                seen.add(nb)
                q.append(path + [nb])

print(shortest("A", "F"))
