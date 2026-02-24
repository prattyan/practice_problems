"""
Day 40: Check Anagram

Question:
Check if two strings are anagrams.
"""

# Solution
def is_anagram(a, b):
    return sorted(a.lower()) == sorted(b.lower())

print(is_anagram("Listen", "Silent"), is_anagram("abc", "abd"))
