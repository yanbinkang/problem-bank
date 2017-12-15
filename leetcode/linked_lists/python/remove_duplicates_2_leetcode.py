from linked_list import *

"""
https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/

Given 1->2->3->3->4->4->5, return 1->2->5

Given 1->1->1->2->3, return 2->3
"""

def delete_duplicates(head):
    previous = None
    current = head

    while current and current.next:
        if current.data != current.next.data:
            previous = current
            current = current.next
        else:
            while current.next and current.next.data == current.data:
                current = current.next
            if previous != None:
                previous.next = current.next
            else:
                head = current.next

            current = current.next

    return head


if __name__ == '__main__':
    a = Node(1)
    b = Node(2)
    c = Node(3)
    d = Node(3)
    e = Node(4)
    f = Node(4)
    g = Node(5)

    a.next = b
    b.next = c
    c.next = d
    d.next = e
    e.next = f
    f.next = g

    # Given 1->2->3->3->4->4->5, return 1->2->5.

    res = delete_duplicates(a)

    while res != None:
        print(str(res.data) + "\n")
        res = res.next


