from linked_list import *

"""
https://leetcode.com/problems/reverse-linked-list/description/

Reverse a singly linked list.

Hint:
A linked list can be reversed either iteratively or recursively. Could you implement both?
"""

def reverse_linked_list(head):
    current = head
    previous = None

    while current:
        next_node = current.next
        current.next = previous
        previous = current
        current = next_node

    return previous

def reverse_list_rec(head):
    return _reverse(head, None)

# 1 -> 2 -> 3 -> None
def _reverse(head, tail):
    if head is None:
        return tail

    next_node = head.next
    head.next = tail
    return _reverse(next_node, head)

if __name__ == '__main__':
    a = Node(1)
    b = Node(2)
    c = Node(3)

    a.next = b
    b.next = c


    d = Node(1)
    e = Node(2)
    f = Node(3)

    d.next = e
    e.next = f

    res = reverse_linked_list(a)
    res1 = reverse_list_rec(d)

    while res:
        print("Node data is %s \n" % (res.data))
        res = res.next

    while res1:
        print(str(res1.data) + "\n")
        res1 = res1.next
