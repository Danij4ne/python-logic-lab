

"""
CH01 - Reverse a Linked List

Description:
    Implement a simple singly linked list and write logic to reverse it.
    The goal is to reverse the order of the nodes so that the last
    becomes first, and so on.

Requirements:
    - Define a Node class with:
        - a value
        - a next pointer (default: None)
    - Create a LinkedList class with:
        - a head pointer
        - a method to add nodes
        - a method to print the list
    - Implement a method reverse() that reverses the linked list.
    - Demonstrate the before and after states.

Notes:
    - No built-in Python lists for reversing.
    - The logic should use pointer manipulation.

Example (expected behavior):
    Original: 1 -> 2 -> 3 -> None
    Reversed: 3 -> 2 -> 1 -> None
"""

# TODO:
# 1. Define the Node class.
# 2. Define the LinkedList class with add, print, and reverse methods.
# 3. Build a sample list.
# 4. Reverse it and print both versions.


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def add(self, value):
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            return

        current = self.head
        while current.next is not None:
            current = current.next

        current.next = new_node

    def print_list(self):
        current = self.head
        while current is not None:
            print(current.value, end=" -> ")
            current = current.next
        print("None")

    def reverse(self):
        prev = None
        current = self.head

        while current is not None:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node

        self.head = prev


# Create a linked list
linked_list = LinkedList()

# Add elements 1, 2, 3
linked_list.add(1)
linked_list.add(2)
linked_list.add(3)

# Print the original list
print("Original:")
linked_list.print_list()

# Reverse the list
linked_list.reverse()

# Print the reversed list
print("Reversed:")
linked_list.print_list()







