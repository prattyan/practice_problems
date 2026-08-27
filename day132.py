"""
Day 132: Longest Palindromic Substring

Question:
Find the longest palindromic substring (expand around center).
"""

# Solution
def longest_pal(s):
    best = ""
    for c in range(len(s)):
        for l, r in ((c, c), (c, c + 1)):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1; r += 1
            if r - l - 1 > len(best):
                best = s[l + 1:r]
    return best

print(longest_pal("babad"), longest_pal("cbbd"))
