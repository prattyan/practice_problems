"""
Day 123: Roman to Integer

Question:
Convert a Roman numeral to an integer.
"""

# Solution
def roman_to_int(s):
    v = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    total = 0
    for i, ch in enumerate(s):
        if i + 1 < len(s) and v[ch] < v[s[i + 1]]:
            total -= v[ch]
        else:
            total += v[ch]
    return total

print(roman_to_int("MCMXCIV"))
