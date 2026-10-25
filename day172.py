"""
Day 172: Word Frequency from a File

Question:
Find the most common words in a text file.
"""

# Solution
import os, tempfile
from collections import Counter

path = os.path.join(tempfile.gettempdir(), "demo_words.txt")
with open(path, "w") as f:
    f.write("the quick brown fox jumps over the lazy dog the end")

words = open(path).read().lower().split()
print(Counter(words).most_common(3))
os.remove(path)
