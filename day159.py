"""
Day 159: Binary Search Tree

Question:
Implement insert and search in a binary search tree.
"""

# Solution
class Node:
    def __init__(self, v):
        self.v, self.left, self.right = v, None, None

def insert(root, v):
    if not root:
        return Node(v)
    if v < root.v:
        root.left = insert(root.left, v)
    else:
        root.right = insert(root.right, v)
    return root

def search(root, v):
    if not root:
        return False
    if v == root.v:
        return True
    return search(root.left if v < root.v else root.right, v)

def inorder(n): return inorder(n.left) + [n.v] + inorder(n.right) if n else []

root = None
for x in (50, 30, 70, 20, 40, 60, 80):
    root = insert(root, x)
print(inorder(root), search(root, 60), search(root, 65))
