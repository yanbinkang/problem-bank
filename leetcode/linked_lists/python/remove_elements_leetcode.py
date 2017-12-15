from linked_list import *

"""
https://leetcode.com/problems/remove-linked-list-elements/

Remove all elements from a linked list of integers that have value val.

Example
Given: 1 --> 2 --> 6 --> 3 --> 4 --> 5 --> 6, val = 6
Return: 1 --> 2 --> 3 --> 4 --> 5
"""

def remove_elements(head, val):
    while head and head.data == val:
        head = head.next

    current = head

    while current and current.next:
        if current.next.data == val:
            current.next = current.next.next
        else:
            current = current.next

    return head

if __name__ == '__main__':
    """
    1 -> 2 -> 6 -> 3 -> 4 -> 5 -> 6

    1 -> 2 -> 3 -> 4 -> 5
    """
    a = Node(1)
    b = Node(2)
    c = Node(6)
    d = Node(3)
    e = Node(4)
    f = Node(5)
    g = Node(6)

    a.next = b
    b.next = c
    c.next = d
    d.next = e
    e.next = f
    f.next = g

    res = remove_elements(a, 6)

    while res:
        print(res.data)
        print("\n")
        res = res.next

