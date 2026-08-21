"""
Day 130: Caesar Cipher

Question:
Encrypt and decrypt text with a Caesar cipher.
"""

# Solution
def caesar(text, shift):
    out = ""
    for ch in text:
        if ch.isalpha():
            base = ord("A") if ch.isupper() else ord("a")
            out += chr((ord(ch) - base + shift) % 26 + base)
        else:
            out += ch
    return out

enc = caesar("Hello, World!", 3)
print(enc, caesar(enc, -3))
