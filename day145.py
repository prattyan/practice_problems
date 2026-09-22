"""
Day 145: Coin Change (Minimum Coins)

Question:
Find the minimum number of coins to make an amount.
"""

# Solution
def coin_change(coins, amount):
    dp = [0] + [float("inf")] * amount
    for a in range(1, amount + 1):
        for c in coins:
            if c <= a:
                dp[a] = min(dp[a], dp[a - c] + 1)
    return dp[amount] if dp[amount] != float("inf") else -1

print(coin_change([1, 5, 10, 25], 63), coin_change([2], 3))
