from linked_list import *

"""
https://leetcode.com/problems/intersection-of-two-linked-lists/

Write a program to find the node at which the intersection of two singly linked lists begins.

For example, the following two linked lists:

A:          a1 -> a2
                   \
                     c1 -> c2 -> c3
                   /
B:     b1 -> b2 -> b3
begin to intersect at node c1.
"""
# import to make leetcode judge pass
import gc
gc.collect()

def get_intersection_node(headA, headB):

    current_a, current_b = headA, headB
    len_a, len_b = 0, 0

    while current_a is not None:
        len_a += 1
        current_a = current_a.next

    while current_b is not None:
        len_b += 1
        current_b = current_b.next

    current_a, current_b = headA, headB

    if len_a > len_b:
        diff = len_a - len_b
        for i in range(diff):
            current_a = current_a.next
    elif len_b > len_a:
        diff = len_b - len_a
        for i in range(diff):
            current_b = current_b.next

    while current_b != current_a:
        current_b = current_b.next
        current_a = current_a.next

    return current_a


if __name__ == '__main__':
    a = Node(3)
    b = Node(6)
    c = Node(9)
    d = Node(15)
    e = Node(30)

    a.next = b
    b.next = c
    c.next = d
    d.next = e

    e = Node(10)
    g = Node(30)

    e.next = d
    d.next = g

    print get_intersection_node(a, e).data
