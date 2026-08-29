"""
Day 134: Run-Length Decoding

Question:
Decode a run-length encoded string like 'a3b2c1'.
"""

# Solution
import re

def decode(s):
    return "".join(ch * int(n) for ch, n in re.findall(r"([A-Za-z])(\d+)", s))

print(decode("a3b2c1"))
