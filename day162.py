"""
Day 162: Graph DFS

Question:
Traverse a graph using depth-first search.
"""

# Solution
graph = {"A": ["B", "C"], "B": ["D", "E"], "C": ["F"], "D": [], "E": ["F"], "F": []}

def dfs(node, seen=None):
    seen = seen if seen is not None else []
    seen.append(node)
    for nb in graph[node]:
        if nb not in seen:
            dfs(nb, seen)
    return seen

print(dfs("A"))
