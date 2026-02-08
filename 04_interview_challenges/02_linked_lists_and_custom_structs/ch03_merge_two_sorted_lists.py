
"""
CH03 - Merge Two Sorted Linked Lists

Description:
    Given two singly linked lists that are already sorted in ascending order,
    merge them into a single sorted linked list.

Requirements:
    - Define a Node class.
    - Define a LinkedList class with:
        - a head pointer
        - a method to add nodes
        - a method to print the list
    - Implement a function merge_sorted_lists(list1, list2) that:
        - takes the heads of two sorted linked lists
        - returns the head of a new merged sorted list
    - Demonstrate the result by printing the merged list.

Notes:
    - The merge should be done by rearranging pointers,
      not by converting to Python lists.
    - Both lists may have different lengths.

Example (expected behavior):
    List 1: 1 -> 3 -> 5 -> None
    List 2: 2 -> 4 -> 6 -> None

    Merged: 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> None
"""

# TODO:
# 1. Define Node and LinkedList classes.
# 2. Implement merge_sorted_lists(list1, list2).
# 3. Create two sorted lists and merge them.
# 4. Print the merged result.

 

# ---------- Node ----------
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


# ---------- LinkedList ----------
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add(self, value):
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return

        self.tail.next = new_node
        self.tail = new_node

    def print_list(self):
        current = self.head
        while current is not None:
            print(current.value, end=" -> ")
            current = current.next
        print("None")


# ---------- Merge function ----------
def merge_sorted_lists(head1, head2):
    dummy = Node(0)
    tail = dummy

    a = head1
    b = head2

    while a is not None and b is not None:
        if a.value <= b.value:
            tail.next = a
            a = a.next
        else:
            tail.next = b
            b = b.next

        tail = tail.next

    # uno de los dos aún puede tener nodos
    if a is not None:
        tail.next = a
    else:
        tail.next = b

    return dummy.next


 
list1 = LinkedList()
list1.add(1)
list1.add(3)
list1.add(5)

list2 = LinkedList()
list2.add(2)
list2.add(4)
list2.add(6)

print("List 1:")
list1.print_list()

print("List 2:")
list2.print_list()

merged_head = merge_sorted_lists(list1.head, list2.head)

merged_list = LinkedList()
merged_list.head = merged_head

print("Merged:")
merged_list.print_list()







        
