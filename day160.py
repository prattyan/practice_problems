"""
Day 160: Height of a Binary Tree

Question:
Compute the height of a binary tree.
"""

# Solution
class Node:
    def __init__(self, v, l=None, r=None):
        self.v, self.left, self.right = v, l, r

def height(n):
    return 0 if not n else 1 + max(height(n.left), height(n.right))

root = Node(1, Node(2, Node(4, Node(7))), Node(3))
print(height(root))
