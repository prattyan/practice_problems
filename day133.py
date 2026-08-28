"""
Day 133: Run-Length Encoding

Question:
Compress a string using run-length encoding.
"""

# Solution
def rle(s):
    out, i = "", 0
    while i < len(s):
        j = i
        while j < len(s) and s[j] == s[i]:
            j += 1
        out += s[i] + str(j - i)
        i = j
    return out

print(rle("aaabbbccd"))
