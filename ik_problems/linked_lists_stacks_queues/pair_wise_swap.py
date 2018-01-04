"""
solution: http://www.geeksforgeeks.org/pairwise-swap-elements-of-a-given-linked-list-by-changing-links/
initial: 1->2->3->4->5->6->7->None
result:  2->1->4->3->6->5->7->None
# 1 -> 2 -> 3 -> 4   =>   2 -> 1 -> 4 -> 3
"""
from sll import *

def pair_wise_swap(head):
    if head == None or head.next == None:
        return head

    prev = head
    current = head.next

    head = current

    while True:
        next_node = current.next
        current.next = prev

        if next_node == None or next_node.next == None:
            prev.next = next_node
            break

        prev.next = next_node.next
        prev = next_node
        current = prev.next

    return head

if __name__ == '__main__':
    a = Node(1)
    b = Node(2)
    c = Node(3)
    d = Node(4)
    e = Node(5)
    f = Node(6)
    g = Node(7)

    a.next = b
    b.next = c
    c.next = d
    d.next = e
    e.next = f
    f.next = g

    res = pair_wise_swap(a)

    while res != None:
        print str(res.data) + "\n"
        res = res.next

