"""
Day 170: Write and Read a File

Question:
Write lines to a text file and read them back.
"""

# Solution
import os, tempfile

path = os.path.join(tempfile.gettempdir(), "demo_notes.txt")
with open(path, "w") as f:
    f.write("Line one\nLine two\nLine three\n")

with open(path) as f:
    for line in f:
        print(line.strip())
os.remove(path)
