"""
Day 131: Longest Common Prefix

Question:
Find the longest common prefix of a list of strings.
"""

# Solution
def lcp(words):
    prefix = words[0]
    for w in words[1:]:
        while not w.startswith(prefix):
            prefix = prefix[:-1]
    return prefix

print(lcp(["flower", "flow", "flight"]))
