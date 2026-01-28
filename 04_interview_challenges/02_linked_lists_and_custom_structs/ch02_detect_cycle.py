
"""
CH02 - Detect Cycle in a Linked List

Description:
    Implement logic to detect whether a singly linked list contains
    a cycle (loop). A cycle exists if a node's "next" pointer eventually
    points back to a previous node instead of reaching None.

Requirements:
    - Define a Node class.
    - Define a LinkedList class with a head pointer.
    - Implement a method has_cycle() that returns True if a cycle exists,
      False otherwise.
    - Demonstrate both cases:
        - A normal list with no cycle.
        - A list where the last node points back to a previous node.

Notes:
    - You may use the "fast and slow pointer" technique (optional).
    - Do NOT use Python lists or sets to track visited nodes (optional challenge).

Example (expected behavior):
    List without cycle: False
    List with cycle: True
"""

# TODO:
# 1. Define Node and LinkedList classes.
# 2. Implement has_cycle() to detect if a cycle exists.
# 3. Demonstrate the method on both a normal and a cyclic list.

class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self, head=None):
        self.head = head

    def has_cycle(self):
        # Caso base: lista vacía o con un solo nodo
        if self.head is None or self.head.next is None:
            return False

        slow = self.head      
        fast = self.head      

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True   

        return False           



a = Node(1)
b = Node(2)
c = Node(3)

a.next = b
b.next = c
c.next = None

lista = LinkedList(a)
print(lista.has_cycle())  # False




