"""
Day 177: Random Password Generator

Question:
Generate a random password with letters, digits and symbols.
"""

# Solution
import random, string

random.seed(42)
chars = string.ascii_letters + string.digits + "!@#$%^&*"
print("".join(random.choice(chars) for _ in range(12)))
