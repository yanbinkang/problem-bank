"""
http://www.geeksforgeeks.org/segregate-even-and-odd-elements-in-a-linked-list/

Method 1
The idea is to get pointer to the last node of list. And then traverse the list starting from the head node and move the odd valued nodes from their current position to end of the list.

Algorithm:
1) Get pointer to the last node.
2) Move all the odd nodes to the end.
    a) Consider all odd nodes before the first even node and move them to end.
    b) Change the head pointer to point to the first even node.
    c) Consider all odd nodes after the first even node and move them to the end.
"""
from sll import *

def segregate_even_odd(head):
    end = head
    prev = None
    current = head

    # get pointer to the last node
    while (end.next != None):
        end = end.next

    new_end = end

    # consoder all odd nodes before the first even node
    # and move them after end
    while current.data % 2 != 0 and current != end:
        new_end.next = current
        current = current.next
        new_end.next.next = None
        new_end = new_end.next

    # do following steps only if there is any even node
    if current.data % 2 == 0:
        head = current
        while current != end:
            if current.data % 2 == 0:
                prev = current
                current = current.next
            else:
                # break the link between prev and current
                prev.next = current.next

                # make next of current None; it's about to be moved to the end
                current.next = None

                # move current to end
                new_end.next = current

                # make current as new end of list
                new_end = current

                # update current pointer to next of the moved node
                current = prev.next
    else:
        prev = current

    if new_end != end and end.data % 2 != 0:
        prev.next = end.next
        end.next = None
        new_end.next = end

    return head


if __name__ == '__main__':
    a = Node(1)
    b = Node(3)
    c = Node(5)
    d = Node(2)
    e = Node(7)
    f = Node(13)
    g = Node(19)

    a.next = b
    b.next = c
    c.next = d
    d.next = e
    e.next = f
    f.next = g

    res = segregate_even_odd(a)

    while res != None:
        print str(res.data) + "\n"
        res = res.next
