"""
Day 164: Cycle in Undirected Graph

Question:
Detect whether an undirected graph contains a cycle.
"""

# Solution
def has_cycle(graph):
    seen = set()

    def dfs(node, parent):
        seen.add(node)
        for nb in graph[node]:
            if nb not in seen:
                if dfs(nb, node):
                    return True
            elif nb != parent:
                return True
        return False

    return any(dfs(n, None) for n in graph if n not in seen)

print(has_cycle({1: [2], 2: [1, 3], 3: [2]}))
print(has_cycle({1: [2, 3], 2: [1, 3], 3: [1, 2]}))
