from linked_list import *

"""
Reverse a linked list from position m to n. Do it in-place and in one-pass.

Given 1->2->3->4->5->NULL, m = 2 and n = 4,

return 1->4->3->2->5->NULL.

The idea is simple and intuitive: find linkedlist [m, n], reverse it, then connect m with n+1, connect n with m-1
"""

def reverse_between(head, m, n):
    if m == n: return head

    dummy_node = Node(0)
    dummy_node.next = head
    prev = dummy_node

    for i in range(m - 1):
        prev = prev.next

    current = prev.next
    reverse = None

    for i in range(n - m + 1):
        next_node = current.next
        current.next = reverse
        reverse = current
        current = next_node

    prev.next.next = current
    prev.next = reverse

    return dummy_node.next





if __name__ == '__main__':
    a = Node(1)
    b = Node(2)
    c = Node(3)
    d = Node(4)
    e = Node(5)

    a.next = b
    b.next = c
    c.next = d
    d.next = e

    res = reverse_between(a, 2, 4)

    while res:
        print(str(res.data) + "\n")
        res = res.next
