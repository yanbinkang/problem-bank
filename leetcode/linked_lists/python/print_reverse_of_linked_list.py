"""
http://www.geeksforgeeks.org/write-a-recursive-function-to-print-reverse-of-a-linked-list/

Given a linked list, print reverse of it using a recursive function. For example, if the given linked list is 1->2->3->4, then output should be 4->3->2->1.
"""
from linked_list import *
def print_reverse_rec(head):
    if head is None: return

    print_reverse_rec(head.next)

    print head.data,

"""
For iterative approach you can reverse linked list in place, then print the reversed linked list. Or use a stack: push the linked list nodes unto the stack till you get to tail. Now pop the stack and print linked list data.
"""


if __name__ == '__main__':
    a = Node(1)
    b = Node(2)
    c = Node(3)
    d = Node(4)

    a.next = b
    b.next = c
    c.next = d

    print_reverse_rec(a)
