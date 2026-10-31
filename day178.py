"""
Day 178: Dice Roll Simulation

Question:
Simulate rolling two dice 1000 times and count outcomes.
"""

# Solution
import random
from collections import Counter

random.seed(1)
rolls = [random.randint(1, 6) + random.randint(1, 6) for _ in range(1000)]
print(sorted(Counter(rolls).items()))
