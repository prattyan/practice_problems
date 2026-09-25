"""
Day 148: 0/1 Knapsack

Question:
Maximize value in a knapsack of given capacity (each item used at most once).
"""

# Solution
def knapsack(weights, values, cap):
    dp = [0] * (cap + 1)
    for w, v in zip(weights, values):
        for c in range(cap, w - 1, -1):
            dp[c] = max(dp[c], dp[c - w] + v)
    return dp[cap]

print(knapsack([1, 3, 4, 5], [1, 4, 5, 7], 7))
