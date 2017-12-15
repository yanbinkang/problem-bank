from linked_list import *

def sort_list(head):
    if head == None:
        return head

    if head.next == None:
        return head

    p1 = head
    p2 = head
    pre = head

    # find middle of list
    while p2 != None and p2.next != None:
        pre = p1
        p1 = p1.next
        p2  = p2.next.next

    # change pre next to None, make two sub lists (head to pre, p1 to p2)
    pre.next = None

    h1 = sort_list(head)
    h2 = sort_list(p1)

    return merge(h1, h2)

def merge(h1, h2):
    if h1 == None:
        return h2

    if h2 == None:
        return h1

    if h1.data < h2.data:
        h1.next = merge(h1.next, h2)
        return h1
    else:
        h2.next = merge(h1, h2.next)
        return h2

if __name__ == '__main__':
    a = Node(5)
    b = Node(23)
    c = Node(29)
    d = Node(6)
    e = Node(12)

    a.next = b
    b.next = c
    c.next = d
    d.next = e

    sorted_list = sort_list(a)

    while sorted_list:
        print(str(sorted_list.data) + "\n")
        sorted_list = sorted_list.next
