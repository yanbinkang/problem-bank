"""
http://www.geeksforgeeks.org/write-a-function-to-get-the-intersection-point-of-two-linked-lists/
1) Get count of the nodes in first list, let count be c1.
2) Get count of the nodes in second list, let count be c2.
3) Get the difference of counts d = abs(c1 - c2)
4) Now traverse the bigger list from the firt node till d nodes so that from here onwards bith the lists have equal no. of nodes.
5) Then we can traverse both the lists in parallel till we come across a common node. (Note that getting a common node is done by comparing the address of the nodes)
"""
from sll import *

def get_intersection_node(head_1, head_2):
    c1 = get_count(head_1)
    c2 = get_count(head_2)

    if c1 > c2:
        d = c1 - c2
        return _get_intersection_node(d, head_1, head_2)
    else:
        d = c2 - c1
        return _get_intersection_node(d, head_2, head_1)

def _get_intersection_node(diff, head_1, head_2):
    current_1 = head_1
    current_2 = head_2

    for i in range(diff):
        if current_1 == None:
            return None
        current_1 = current_1.next

    while current_1 != None and current_2 != None:
        if current_1.data == current_2.data:
            return current_1.data
        current_1 = current_1.next
        current_2 = current_2.next

    return None

def get_count(head):
    count = 0
    current = head

    while current != None:
        count += 1
        current = current.next

    return count

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
f = Node(15)
g = Node(30)

e.next = f
f.next = g

print get_intersection_node(a, e)
