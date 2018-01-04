"""
actual solution: http://programming-puzzle.blogspot.com/2014/02/zip-of-linked-list.html
Similar to this solution
http://www.geeksforgeeks.org/merge-a-linked-list-into-another-linked-list-at-alternate-positions/

1. Split list from middle into two lists
2. Reverse second list
3. Merge two lists by picking one node from each list at a time.
"""
from sll import *

def zip_linked_list(head):
    current_1 = head
    current_2 = split_list(head)
    current_2 = reverse_list(current_2)

    new_head = current_1

    while current_1 != None and current_2 != None:
        c1_next = current_1.next
        c2_next = current_2.next

        current_2.next = c1_next
        current_1.next = current_2

        current_1 = c1_next
        current_2 = c2_next

    return new_head

    # 1->2->3->None
    # 6->5->4->None

def split_list(head):
    if head == None:
        return None

    slow = head
    fast = head.next

    while fast != None and fast.next != None:
        slow = slow.next
        fast = fast.next.next


    new_head = slow.next
    slow.next = None
    return new_head

def reverse_list(head):
    previous = None
    current = head
    new_next = None

    while current != None:
        new_next = current.next
        current.next = previous
        previous = current
        current = new_next

    return previous

a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)
e = Node(5)
f = Node(6)

a.next = b
b.next = c
c.next = d
d.next = e
e.next = f

zipp = zip_linked_list(a)

while zipp != None:
    print str(zipp.data) + "\n"
    zipp = zipp.next
