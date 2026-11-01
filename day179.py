"""
Day 179: Number Guessing Game (Simulated)

Question:
Write a number guessing game; here the guesses are automated with binary search.
"""

# Solution
secret = 73
lo, hi, tries = 1, 100, 0
while True:
    guess = (lo + hi) // 2
    tries += 1
    if guess == secret:
        print(f"Guessed {secret} in {tries} tries")
        break
    elif guess < secret:
        lo = guess + 1
    else:
        hi = guess - 1
