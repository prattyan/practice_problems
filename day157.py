"""
Day 157: Reverse a Linked List

Question:
Reverse a singly linked list.
"""

# Solution
class Node:
    def __init__(self, data, nxt=None):
        self.data, self.next = data, nxt

def reverse(head):
    prev = None
    while head:
        head.next, prev, head = prev, head, head.next
    return prev

head = Node(1, Node(2, Node(3, Node(4))))
head = reverse(head)
out = []
while head:
    out.append(head.data)
    head = head.next
print(out)
