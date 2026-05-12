"""
Day 100: Majority Element

Question:
Find the element that appears more than n/2 times (Boyer-Moore).
"""

# Solution
def majority(a):
    cand, cnt = None, 0
    for x in a:
        if cnt == 0:
            cand = x
        cnt += 1 if x == cand else -1
    return cand

print(majority([2, 2, 1, 1, 1, 2, 2]))
