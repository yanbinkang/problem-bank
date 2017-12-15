from linked_list import *

"""
https://leetcode.com/problems/partition-list/

Given a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.

You should preserve the original relative order of the nodes in each of the two partitions.

For example,
Given 1->4->3->2->5->2 and x = 3,
return 1->2->2->4->3->5.

solution:
1. separate the list into 2 distinct lists and link them afterwards.

2. p1, p2 traverses the list and hd1 and hd2 are the heads of two lists
"""
def partition(head, x):
    dummy_node_1 = p1 = Node(0)
    dummy_node_2 = p2 = Node(0)

    while head != None:
        if head.data < x:
            p1.next = head
            p1 = p1.next
        else:
            p2.next = head
            p2 = p2.next

        head = head.next

    # join the lists
    p2.next = None # end the second list
    p1.next = dummy_node_2.next # join first list to second list
    return dummy_node_1.next

if __name__ == '__main__':
    a = Node(1)
    b = Node(4)
    c = Node(3)
    d = Node(2)
    e = Node(5)
    f = Node(2)

    a.next = b
    b.next = c
    c.next = d
    d.next = e
    e.next = f

    res = partition(a, 3)

    while res is not None:
        print(str(res.data) + "\n")
        res = res.next
