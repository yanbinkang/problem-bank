from sll import *
"""
question: reverse a linked list in groups of given size
ref: http://www.geeksforgeeks.org/reverse-a-list-in-groups-of-given-size/

input:   1->2->3->4->5->6->7->8->None and k = 3
output:  3->2->1->6->5->4->8->7->None

input:   1->2->3->4->5->6->7->8->None and k = 5
output   5->4->3->2->1->8->7->6->None
"""
def reverse(head, k):
    current = head
    prev = None
    new_next = None
    count = 0

    while current != None and count < k:
        new_next = current.next
        current.next = prev
        prev = current
        current = new_next
        count += 1

    """
    new_next is now a pointer to (k + 1)th node
    Recursive call for the list starting from current.
    And make rest of the list as next of first node
    """

    if new_next != None:
        head.next = reverse(new_next, k)

    # prev is new head of list
    return prev

if __name__ == '__main__':
    a = Node(1)
    b = Node(2)
    c = Node(3)
    d = Node(4)
    e = Node(5)
    f = Node(6)
    g = Node(7)
    h = Node(8)

    a.next = b
    b.next = c
    c.next = d
    d.next = e
    e.next = f
    f.next = g
    g.next = h

    res = reverse(a, 5)

    while res != None:
        print str(res.data) + "\n"
        res = res.next
