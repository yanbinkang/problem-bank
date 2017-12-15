from linked_list import *
"""
https://leetcode.com/problems/swap-nodes-in-pairs/

Given 1->2->3->4, you should return the list as 2->1->4->3
"""
def swap_pairs(head):
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

    res = swap_pairs(a)

    while res != None:
        print str(res.data) + "\n"
        res = res.next
