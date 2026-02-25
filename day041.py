"""
Day 41: Character Frequency

Question:
Count the frequency of each character in a string.
"""

# Solution
s = "mississippi"
freq = {}
for ch in s:
    freq[ch] = freq.get(ch, 0) + 1
print(freq)
