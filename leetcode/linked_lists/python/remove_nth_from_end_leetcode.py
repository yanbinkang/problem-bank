from linked_list import *

"""
https://leetcode.com/problems/remove-nth-node-from-end-of-list/

Given a linked list, remove the nth node from the end of list and return its head.

For example,

   Given linked list: 1->2->3->4->5, and n = 2.

   After removing the second node from the end, the linked list becomes 1->2->3->5.
"""
def remove_nth_from_end(head, n):
    slow, fast = head, head

    for i in range(n):
        fast = fast.next
        if fast is None:
            return head.next

    while fast.next is not None:
        fast = fast.next
        slow = slow.next

    slow.next = slow.next.next

    return head


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

    res = remove_nth_from_end(a, 2)

    while res:
        print(str(res.data) + "\n")
        res = res.next
