"""
Day 171: Count Lines, Words and Characters in a File

Question:
Count lines, words and characters of a text file.
"""

# Solution
import os, tempfile

path = os.path.join(tempfile.gettempdir(), "demo_count.txt")
with open(path, "w") as f:
    f.write("Python is great\nFiles are easy to handle\n")

text = open(path).read()
print("Lines:", len(text.splitlines()))
print("Words:", len(text.split()))
print("Chars:", len(text))
os.remove(path)
