from sll import *

def middle_of_linked_list(head):
    if head == None or head.next == None:
        return head.data

    slow = head
    fast = head.next

    while fast != None and fast.next != None:
        slow = slow.next
        fast = fast.next.next

    return slow.data

if __name__ == '__main__':
    a = Node(1)
    b = Node(32)
    c = Node(12)
    d = Node(1)
    e = Node(5)

    a.next = b
    b.next = c
    c.next = d
    d.next = e

    print middle_of_linked_list(a)
