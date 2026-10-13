"""
Day 158: Binary Tree Inorder Traversal

Question:
Build a binary tree and print its inorder, preorder and postorder traversals.
"""

# Solution
class Node:
    def __init__(self, v):
        self.v, self.left, self.right = v, None, None

def inorder(n): return inorder(n.left) + [n.v] + inorder(n.right) if n else []
def preorder(n): return [n.v] + preorder(n.left) + preorder(n.right) if n else []
def postorder(n): return postorder(n.left) + postorder(n.right) + [n.v] if n else []

root = Node(1)
root.left, root.right = Node(2), Node(3)
root.left.left, root.left.right = Node(4), Node(5)
print(inorder(root), preorder(root), postorder(root))
