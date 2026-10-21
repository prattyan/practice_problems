"""
Day 166: Number of Islands

Question:
Count islands (connected groups of 1s) in a grid.
"""

# Solution
def islands(grid):
    rows, cols = len(grid), len(grid[0])
    seen = set()

    def dfs(r, c):
        if r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] == 0 or (r, c) in seen:
            return
        seen.add((r, c))
        for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            dfs(r + dr, c + dc)

    count = 0
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1 and (r, c) not in seen:
                dfs(r, c)
                count += 1
    return count

print(islands([[1, 1, 0, 0], [0, 1, 0, 1], [1, 0, 0, 1], [0, 0, 1, 1]]))
