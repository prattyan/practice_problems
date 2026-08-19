"""
Day 129: Reverse Words in a Sentence

Question:
Reverse the order of words in a sentence.
"""

# Solution
s = "I love Python programming"
print(" ".join(s.split()[::-1]))
