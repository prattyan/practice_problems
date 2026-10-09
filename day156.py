"""
Day 156: Singly Linked List

Question:
Implement a singly linked list with append and display.
"""

# Solution
class Node:
    def __init__(self, data):
        self.data, self.next = data, None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        node = Node(data)
        if not self.head:
            self.head = node
            return
        cur = self.head
        while cur.next:
            cur = cur.next
        cur.next = node

    def to_list(self):
        out, cur = [], self.head
        while cur:
            out.append(cur.data)
            cur = cur.next
        return out

ll = LinkedList()
for x in (10, 20, 30):
    ll.append(x)
print(ll.to_list())
