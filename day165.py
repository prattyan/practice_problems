"""
Day 165: Dijkstra's Shortest Path

Question:
Find shortest distances from a source in a weighted graph.
"""

# Solution
import heapq

graph = {"A": [("B", 4), ("C", 2)], "B": [("D", 5)], "C": [("B", 1), ("D", 8)], "D": []}

def dijkstra(src):
    dist = {n: float("inf") for n in graph}
    dist[src] = 0
    pq = [(0, src)]
    while pq:
        d, u = heapq.heappop(pq)
        if d > dist[u]:
            continue
        for v, w in graph[u]:
            if d + w < dist[v]:
                dist[v] = d + w
                heapq.heappush(pq, (dist[v], v))
    return dist

print(dijkstra("A"))
